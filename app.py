import os
import sys
import time
import uuid
import secrets
import re
import logging
from datetime import timedelta
from functools import wraps
from urllib.parse import quote_plus
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from google import genai
import markdown

from database import (
    init_db,
    save_assessment,
    get_all_assessments,
    get_assessment_stats,
    get_assessment_by_id,
    get_latest_assessment,
    get_latest_assessments_by_subject,
    add_bookmark,
    remove_bookmark,
    get_all_bookmarks,
    clear_history,
    create_user,
    get_user_by_email,
    get_user_by_id,
    transfer_guest_data_to_user,
    verify_assessment_ownership,
    save_study_plan,
    get_latest_study_plan,
    get_study_plan_by_id,
    update_study_plan_tasks
)
from questions import SUBJECTS, get_all_subjects, get_subject
from knowledge_base import generate_offline_study_guide, generate_seven_day_study_plan
from resources import (
    get_all_resources,
    get_resource_by_id,
    filter_resources,
    get_recommended_resources_for_assessment,
    get_popular_starter_resources,
    get_subjects_and_topics_map
)
try:
    from ml_model import analyze_topic_learning_patterns
except Exception:
    analyze_topic_learning_patterns = None

# Load environment variables
load_dotenv()

# Setup robust, crash-resilient application logger
logger = logging.getLogger("learngap")
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def safe_log(msg, level="info"):
    """
    Safely writes log messages without ever raising OSError / Errno 5 I/O errors
    even if the terminal, pipe, or stdout/stderr is closed or detached.
    """
    try:
        if level == "error":
            logger.error(msg)
        elif level == "warning":
            logger.warning(msg)
        else:
            logger.info(msg)
    except Exception:
        # Fallback to sys.stderr or pass silently to prevent crashing requests
        try:
            sys.stderr.write(f"{msg}\n")
        except Exception:
            pass


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "learngap_secret_key_2026")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False,
    PERMANENT_SESSION_LIFETIME=timedelta(days=14),
)

# Ensure database schema is initialized and migrated
init_db()

# --------------------------------------------------
# Auth, Session & CSRF Security Helpers
# --------------------------------------------------

def get_session_context():
    """
    Returns (current_user, user_id, guest_session_id, is_guest).
    Guarantees that an anonymous visitor receives a unique, isolated guest_session_id.
    """
    user_id = session.get("user_id")
    if user_id:
        user = get_user_by_id(user_id)
        if user:
            return user, user["id"], None, False
        else:
            session.pop("user_id", None)

    guest_session_id = session.get("guest_session_id")
    if not guest_session_id:
        guest_session_id = str(uuid.uuid4())
        session["guest_session_id"] = guest_session_id
        session.permanent = True

    return None, None, guest_session_id, True


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user, user_id, guest_session_id, is_guest = get_session_context()
        if not user:
            flash("Please sign in to access your student account.", "warning")
            return redirect(url_for("login", next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def generate_csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return session["csrf_token"]


def validate_csrf(token):
    session_token = session.get("csrf_token")
    if not session_token or not token:
        return False
    return secrets.compare_digest(session_token, token)


@app.context_processor
def inject_global_template_vars():
    user, user_id, guest_session_id, is_guest = get_session_context()
    token = generate_csrf_token()
    return {
        "current_user": user,
        "is_guest": is_guest,
        "guest_session_id": guest_session_id,
        "csrf_token": token
    }

# --------------------------------------------------
# Gemini Client & Cascading Configuration
# --------------------------------------------------

CANDIDATE_MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-flash-lite-latest",
    "gemini-flash-latest"
]


def build_ai_prompt(subject_name, score, total, topic_results, weak_topics,
                    strong_topics, strongest_topic, weakest_topic, recommended_resources=None,
                    ml_analysis=None):
    """
    Constructs a precise educational prompt for Gemini based on actual assessment results,
    ML learning pattern analysis, and verified learning resources from LearnGap's catalogue.
    """
    topic_summary_lines = [f"- {t['topic']}: {t['score']}% ({t['status']})" for t in topic_results]
    topic_summary_text = "\n".join(topic_summary_lines)

    ml_context = ""
    if ml_analysis and ml_analysis.get("formatted_summary"):
        ml_context = f"\n{ml_analysis['formatted_summary']}\n"

    resources_context = ""
    if recommended_resources:
        res_lines = [f"- {r['title']} ({r['resource_type']} by {r['provider']})" for r in recommended_resources[:4]]
        resources_context = (
            "\nRecommended Verified Resources from LearnGap Catalogue:\n" +
            "\n".join(res_lines) +
            "\nPlease specifically suggest these actual resources in your study plan."
        )

    if weak_topics:
        weak_list_text = ", ".join(weak_topics)
        prompt = f"""
You are LearnGap's AI Study Coach for a college student.

The student recently completed a {subject_name} assessment.

Assessment Results:
- Overall Score: {score}/{total} ({int((score/total)*100)}%)
- Strongest Topic on this assessment: {strongest_topic or 'N/A'}
- Priority Topic needing attention: {weakest_topic or 'N/A'}

Topic Performance Breakdown:
{topic_summary_text}
{ml_context}
Topics requiring attention:
{weak_list_text}
{resources_context}

Instructions:
1. Use only the supplied assessment results. Do not invent scores, answers, or external history.
2. Provide brief, encouraging overall feedback acknowledging their effort.
3. Focus your detailed coaching specifically on the topics that need improvement ({weak_list_text}).
4. For each weak or needs-improvement topic, provide:
   • What the topic means in simple words
   • 3 important concepts to remember
   • 2 quick hints or memory hooks
   • 2 common mistakes students make
   • A practical recommendation for what to practice next
5. Provide a realistic short study plan incorporating the verified learning resources listed above.
6. Avoid lengthy explanations of topics where the student already scored strongly.
7. Do not claim that a student has mastered a topic based only on two questions; describe results as performance on this assessment.
8. Keep language clear, educational, structured with clean markdown headings and bullet points.
"""
    else:
        prompt = f"""
You are LearnGap's AI Study Coach for a college student.

The student completed a {subject_name} assessment and achieved a perfect or strong score across all topics.

Assessment Results:
- Overall Score: {score}/{total} ({int((score/total)*100)}%)

Topic Performance Breakdown:
{topic_summary_text}
{ml_context}
{resources_context}

Instructions:
1. All assessed topics in {subject_name} were answered correctly or strongly on this assessment. Do not invent learning gaps.
2. Provide positive, factual feedback on their solid execution.
3. Highlight 2-3 important advanced concepts to explore next in {subject_name}.
4. Provide 3 practical challenge suggestions or real-world project ideas to deepen their knowledge, mentioning the verified learning resources.
5. Provide one recommended next topic or technical direction for going to the next level.
6. Do not claim absolute lifelong mastery; describe the result as strong performance on this assessment.
7. Use clear headings, bullet points, and an encouraging, professional tone.
"""
    return prompt.strip()


def get_ai_coach_guidance(subject_name, score, total, topic_results,
                          weak_topics, strong_topics, strongest_topic, weakest_topic,
                          recommended_resources=None, ml_analysis=None):
    """
    Attempts to generate AI Study Coach advice using the Gemini API.
    Cascades through reliable models with backoff retry.
    Falls back gracefully to the subject-specific offline knowledge base if unavailable.
    Guaranteed never to crash the caller.
    """
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        client = None

        if api_key:
            try:
                client = genai.Client(api_key=api_key)
            except Exception as e:
                safe_log(f"[AI Coach] Gemini client initialization error: {e}", level="warning")

        prompt = build_ai_prompt(
            subject_name=subject_name,
            score=score,
            total=total,
            topic_results=topic_results,
            weak_topics=weak_topics,
            strong_topics=strong_topics,
            strongest_topic=strongest_topic,
            weakest_topic=weakest_topic,
            recommended_resources=recommended_resources,
            ml_analysis=ml_analysis
        )

        gemini_text = None

        if client:
            for model_name in CANDIDATE_MODELS:
                safe_log(f"[AI Coach] Attempting {subject_name} guidance via {model_name}...")
                for attempt in range(2):
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt
                        )
                        if response and response.text:
                            gemini_text = response.text
                            safe_log(f"[AI Coach] Success with model: {model_name}")
                            break
                    except Exception as err:
                        err_str = str(err)
                        safe_log(f"[AI Coach] {model_name} attempt {attempt + 1} warning: {err_str[:120]}", level="warning")
                        if attempt == 0 and ("503" in err_str or "429" in err_str):
                            time.sleep(1.0)
                        else:
                            break

                if gemini_text:
                    break

        if gemini_text:
            try:
                badge = (
                    '<div class="ai-source-badge online-ai-badge" style="margin-bottom: 20px;">'
                    '<span class="badge-pill badge-green" style="font-size: 12.5px; font-weight: 700; padding: 6px 16px; display: inline-flex; align-items: center; gap: 7px; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.2);">'
                    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
                    '<path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>'
                    '</svg> Personalized Gemini AI Guidance</span></div>\n\n'
                )
                return badge + markdown.markdown(gemini_text, extensions=["extra", "nl2br"])
            except Exception as md_err:
                safe_log(f"[AI Coach] Markdown parsing error on Gemini response: {md_err}", level="warning")
    except Exception as outer_err:
        safe_log(f"[AI Coach] Unexpected error during AI generation: {outer_err}", level="warning")

    # Graceful Offline Knowledge Fallback
    safe_log(f"[AI Coach] Gemini unavailable for {subject_name}. Serving curated offline knowledge base.")
    try:
        offline_md = generate_offline_study_guide(
            subject_name=subject_name,
            score=score,
            total=total,
            weak_topics=weak_topics
        )
        badge = (
            '<div class="ai-source-badge offline-ai-badge" style="margin-bottom: 20px;">'
            '<span class="badge-pill badge-neutral" style="background: #EAF2F8; color: var(--navy-900); border: 1px solid var(--border-medium); font-size: 12.5px; font-weight: 700; padding: 6px 16px; display: inline-flex; align-items: center; gap: 7px;">'
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>'
            '<path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>'
            '</svg> Curated Offline Study Coach Guidance (AI Offline)</span></div>\n\n'
        )
        return badge + markdown.markdown(offline_md, extensions=["extra", "nl2br"])
    except Exception as fallback_err:
        safe_log(f"[AI Coach] Offline guide generation error: {fallback_err}", level="error")
        return f'<div class="ai-source-badge offline-ai-badge" style="margin-bottom: 20px;"><span class="badge-pill badge-neutral">Curated Diagnostic Feedback</span></div><p>Great effort on the {subject_name} diagnostic assessment ({score}/{total}). Review your topic performance breakdown below to target your conceptual revision.</p>'


def get_enriched_subjects(user_id=None, guest_session_id=None):
    """Returns all subjects enriched with real database attempt counts, best scores, and latest scores scoped to user or guest."""
    stats = get_assessment_stats(user_id=user_id, guest_session_id=guest_session_id)
    stats_by_id = {s["subject_id"]: s for s in stats.get("subject_stats", [])}
    latest_by_id = get_latest_assessments_by_subject(user_id=user_id, guest_session_id=guest_session_id)
    all_subs = get_all_subjects()
    enriched = []
    for s in all_subs:
        s_copy = dict(s)
        match = stats_by_id.get(s["id"])
        latest_match = latest_by_id.get(s["id"])
        if match:
            s_copy["attempt_count"] = match["attempt_count"]
            s_copy["best_pct"] = match["best_pct"]
            s_copy["has_attempted"] = True
        else:
            s_copy["attempt_count"] = 0
            s_copy["best_pct"] = 0
            s_copy["has_attempted"] = False

        if latest_match:
            s_copy["latest_score"] = latest_match["score"]
            s_copy["latest_total"] = latest_match["total"]
            s_copy["latest_pct"] = latest_match["percentage"]
            s_copy["latest_date"] = latest_match["created_at"]
        else:
            s_copy["latest_score"] = None
            s_copy["latest_total"] = None
            s_copy["latest_pct"] = None
            s_copy["latest_date"] = None

        enriched.append(s_copy)
    return enriched


def get_dashboard_analytics(user_id=None, guest_session_id=None):
    """
    Computes comprehensive student learning analytics scoped to user or guest session.
    Calculates:
      1. Four summary statistics: Total Assessments, Average Score, Best Score, Weakest Subject
      2. Subject Performance across all six subjects (with attempt count, avg score, best score, latest score)
      3. Topic Performance aggregation and horizontal bar visualization data
      4. K-Means ML Learning Pattern Analysis (Strong Performance, Developing, Priority for Improvement)
      5. Recommended Focus based on weakest topic/area
      6. Chronological Progress History
    Guarantees strict data isolation and never uses hard-coded placeholder values.
    """
    stats = get_assessment_stats(user_id=user_id, guest_session_id=guest_session_id)
    history = get_all_assessments(limit=50, user_id=user_id, guest_session_id=guest_session_id)
    all_subjects = get_enriched_subjects(user_id=user_id, guest_session_id=guest_session_id)
    latest = get_latest_assessment(user_id=user_id, guest_session_id=guest_session_id)

    total_assessments = stats.get("total_assessments", 0)
    has_data = total_assessments > 0 and len(history) > 0

    # 1. Four Summary Statistics
    if has_data:
        avg_score = stats.get("average_score", 0)
        avg_score_display = f"{avg_score}%"
        best_score = max((h["percentage"] for h in history), default=0)
        best_score_display = f"{best_score}%"
    else:
        avg_score = 0
        avg_score_display = "—"
        best_score = 0
        best_score_display = "—"

    # 2. Subject Performance across all 6 core subjects
    for s in all_subjects:
        sub_scores = [h["percentage"] for h in history if h.get("subject_id") == s["id"]]
        if sub_scores:
            s["avg_score"] = round(sum(sub_scores) / len(sub_scores), 1)
            s["attempt_count"] = len(sub_scores)
            s["has_attempted"] = True
            s["best_score"] = max(sub_scores)
            if s["avg_score"] >= 70:
                s["tier_class"] = "bar-fill-strong"
                s["status_badge"] = "badge-green"
                s["status_text"] = "Strong"
            elif s["avg_score"] >= 50:
                s["tier_class"] = "bar-fill-improve"
                s["status_badge"] = "badge-amber"
                s["status_text"] = "Developing"
            else:
                s["tier_class"] = "bar-fill-weak"
                s["status_badge"] = "badge-red"
                s["status_text"] = "Needs Focus"
        else:
            s["avg_score"] = None
            s["attempt_count"] = 0
            s["has_attempted"] = False
            s["best_score"] = None
            s["tier_class"] = ""
            s["status_badge"] = "badge-neutral"
            s["status_text"] = "Not Attempted"

    # Identify Weakest Subject
    attempted_subs = [s for s in all_subjects if s["has_attempted"]]
    if attempted_subs:
        weakest_sub = min(attempted_subs, key=lambda s: (s["avg_score"], s["name"]))
        weakest_subject_name = weakest_sub["name"]
        weakest_subject_score = weakest_sub["avg_score"]
        weakest_subject_display = f"{weakest_sub['name']} ({weakest_sub['avg_score']}%)"
    else:
        weakest_subject_name = "None"
        weakest_subject_score = None
        weakest_subject_display = "—"

    # 3. Topic Performance Visualization Data
    topic_map = {}
    for h in history:
        t_results = h.get("topic_results") or []
        for tr in t_results:
            t_name = tr.get("topic")
            if not t_name:
                continue
            if t_name not in topic_map:
                topic_map[t_name] = {
                    "topic": t_name,
                    "subject_id": h.get("subject_id"),
                    "subject_name": h.get("subject_name"),
                    "correct": 0,
                    "total": 0,
                    "scores": []
                }
            topic_map[t_name]["correct"] += tr.get("correct", 0)
            topic_map[t_name]["total"] += tr.get("total", 0)
            topic_map[t_name]["scores"].append(tr.get("score", 0))

    topic_performance = []
    for t_name, t_data in topic_map.items():
        if t_data["total"] > 0:
            score_pct = round((t_data["correct"] / t_data["total"]) * 100)
        elif t_data["scores"]:
            score_pct = round(sum(t_data["scores"]) / len(t_data["scores"]))
        else:
            score_pct = 0

        if score_pct >= 70:
            status = "Strong"
            tier_class = "bar-fill-strong"
            badge_class = "badge-green"
        elif score_pct >= 50:
            status = "Developing"
            tier_class = "bar-fill-improve"
            badge_class = "badge-amber"
        else:
            status = "Priority for Improvement"
            tier_class = "bar-fill-weak"
            badge_class = "badge-red"

        topic_performance.append({
            "topic": t_name,
            "subject_id": t_data["subject_id"],
            "subject_name": t_data["subject_name"],
            "score": score_pct,
            "correct": t_data["correct"],
            "total": t_data["total"],
            "status": status,
            "tier_class": tier_class,
            "badge_class": badge_class
        })

    # Sort topics: lowest score first so priority gaps are prominent
    topic_performance.sort(key=lambda x: (x["score"], x["topic"]))

    # 4. Learning Pattern Analysis (K-Means ML)
    ml_analysis = None
    if topic_performance and analyze_topic_learning_patterns:
        try:
            ml_input = [{"topic": t["topic"], "score": t["score"]} for t in topic_performance]
            ml_analysis = analyze_topic_learning_patterns(ml_input)
        except Exception as ml_err:
            safe_log(f"[ML Model] Error analyzing topic patterns in dashboard: {ml_err}", level="warning")
            ml_analysis = None

    if not ml_analysis:
        from ml_model import _create_empty_result
        ml_analysis = _create_empty_result(
            status="insufficient_data",
            message="Complete diagnostic assessments across topics to activate K-Means pattern clustering."
        )

    # 5. Recommended Focus
    if topic_performance:
        weakest_topic_item = topic_performance[0]  # lowest score
        if weakest_topic_item["score"] < 70:
            rec_topic = weakest_topic_item["topic"]
            rec_sub_id = weakest_topic_item["subject_id"]
            rec_sub_name = weakest_topic_item["subject_name"]
            rec_score = weakest_topic_item["score"]
            recommended_focus = {
                "topic": rec_topic,
                "subject_id": rec_sub_id,
                "subject_name": rec_sub_name,
                "score": rec_score,
                "text": f"Focus on {rec_topic} and related concepts.",
                "detail": f"Based on your diagnostic assessment data, {rec_topic} currently has the lowest accuracy ({rec_score}%). Dedicated practice in this area will yield the greatest performance improvement.",
                "resource_url": f"/resources?subject={rec_sub_id}&topic={quote_plus(rec_topic)}"
            }
        else:
            recommended_focus = {
                "topic": None,
                "subject_id": None,
                "subject_name": None,
                "score": None,
                "text": "All assessed topics satisfy the mastery threshold (≥70%).",
                "detail": "Outstanding mastery across all evaluated topics! Continue challenging yourself with advanced projects and cross-disciplinary concepts.",
                "resource_url": "/subjects"
            }
    else:
        recommended_focus = {
            "topic": None,
            "subject_id": None,
            "subject_name": None,
            "score": None,
            "text": "Complete a diagnostic assessment to identify your key learning gaps.",
            "detail": "Take a 10-question assessment in any of the 6 core subjects to activate personalized focus guidance.",
            "resource_url": "/subjects"
        }

    # 6. Progress History (chronological order)
    chronological_history = list(reversed(history))
    has_enough_history = len(chronological_history) >= 2

    return {
        "total_assessments": total_assessments,
        "has_data": has_data,
        "avg_score": avg_score,
        "avg_score_display": avg_score_display,
        "best_score": best_score,
        "best_score_display": best_score_display,
        "weakest_subject_name": weakest_subject_name,
        "weakest_subject_score": weakest_subject_score,
        "weakest_subject_display": weakest_subject_display,
        "subjects": all_subjects,
        "topic_performance": topic_performance,
        "ml_analysis": ml_analysis,
        "recommended_focus": recommended_focus,
        "chronological_history": chronological_history,
        "has_enough_history": has_enough_history,
        "latest": latest,
        "raw_stats": stats
    }


# --------------------------------------------------
# Routes: Core & Navigation
# --------------------------------------------------

@app.route("/")
@app.route("/dashboard")
def home():
    """Home / SaaS Dashboard page with real database metrics and comprehensive learning analytics."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    analytics = get_dashboard_analytics(user_id=user_id, guest_session_id=guest_session_id)
    stats = analytics["raw_stats"]
    latest = analytics["latest"]
    recent_assessments = get_all_assessments(limit=3, user_id=user_id, guest_session_id=guest_session_id)
    all_subjects = analytics["subjects"]

    return render_template(
        "index.html",
        stats=stats,
        analytics=analytics,
        latest=latest,
        recent_assessments=recent_assessments,
        subjects=all_subjects,
        is_guest=is_guest
    )


@app.route("/subjects")
def subjects():
    """Subject selection catalog containing all 6 active subjects with real progress."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    all_subjects = get_enriched_subjects(user_id=user_id, guest_session_id=guest_session_id)
    return render_template("subjects.html", subjects=all_subjects)


@app.route("/quiz/<subject_id>")
def quiz(subject_id):
    """Conducts a topic-wise assessment for any of the 6 subjects."""
    subject = get_subject(subject_id)
    if not subject:
        return redirect(url_for("subjects"))

    return render_template(
        "quiz.html",
        subject=subject,
        questions=subject["questions"]
    )


# --------------------------------------------------
# Routes: Student Authentication & Guest Mode
# --------------------------------------------------

@app.route("/guest")
def guest_mode():
    """Explicitly navigates in Guest Mode with an isolated session identifier."""
    if session.get("user_id"):
        session.pop("user_id", None)
    if "guest_session_id" not in session:
        session["guest_session_id"] = str(uuid.uuid4())
    session.permanent = True
    flash("You are exploring LearnGap as a Guest. Take any assessment freely without registration!", "info")
    return redirect(url_for("subjects"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Student sign-in with secure password verification and CSRF protection."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    if user:
        return redirect(url_for("account"))

    if request.method == "POST":
        token = request.form.get("csrf_token")
        if not validate_csrf(token):
            flash("Session security token expired. Please try submitting again.", "error")
            return render_template("login.html"), 400

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Please enter both your email address and password.", "error")
            return render_template("login.html", email=email), 400

        existing_user = get_user_by_email(email)
        if not existing_user or not check_password_hash(existing_user["password_hash"], password):
            flash("Invalid email or password. Please verify your credentials and try again.", "error")
            return render_template("login.html", email=email), 401

        # Successful authentication
        guest_id_to_transfer = session.get("guest_session_id")
        session.clear()
        session["user_id"] = existing_user["id"]
        session.permanent = True

        transferred = 0
        if guest_id_to_transfer:
            transferred = transfer_guest_data_to_user(guest_id_to_transfer, existing_user["id"])

        if transferred > 0:
            flash(f"Welcome back, {existing_user['name']}! {transferred} assessment(s) from your guest session were transferred to your account.", "success")
        else:
            flash(f"Welcome back, {existing_user['name']}!", "success")

        next_page = request.args.get("next")
        if next_page and next_page.startswith("/"):
            return redirect(next_page)
        return redirect(url_for("account"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Student registration route with secure input validation, salted hashing, and guest data transfer."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    if user:
        return redirect(url_for("account"))

    guest_records_count = 0
    if guest_session_id:
        guest_assessments = get_all_assessments(guest_session_id=guest_session_id)
        guest_records_count = len(guest_assessments)

    if request.method == "POST":
        token = request.form.get("csrf_token")
        if not validate_csrf(token):
            flash("Session security token expired. Please try submitting again.", "error")
            return render_template("register.html", guest_records_count=guest_records_count), 400

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or len(name) < 2:
            flash("Please enter a valid student name (at least 2 characters).", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 400

        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(email_pattern, email):
            flash("Please enter a valid email address.", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 400

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 400

        if password != confirm_password:
            flash("Passwords do not match. Please re-enter your password.", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 400

        existing_user = get_user_by_email(email)
        if existing_user:
            flash("An account with this email address already exists. Please sign in instead.", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 400

        password_hash = generate_password_hash(password, method="pbkdf2:sha256")
        new_user = create_user(email=email, password_hash=password_hash, name=name)
        if not new_user:
            flash("An unexpected error occurred while creating your account. Please try again.", "error")
            return render_template("register.html", name=name, email=email, guest_records_count=guest_records_count), 500

        transferred = 0
        if guest_session_id:
            transferred = transfer_guest_data_to_user(guest_session_id, new_user["id"])

        session.clear()
        session["user_id"] = new_user["id"]
        session.permanent = True

        if transferred > 0:
            flash(f"Account created successfully! We preserved and transferred {transferred} assessment(s) from your guest session into your new account.", "success")
        else:
            flash("Welcome to LearnGap! Your student account is now active.", "success")

        return redirect(url_for("account"))

    return render_template("register.html", guest_records_count=guest_records_count)


@app.route("/logout")
def logout():
    """Signs out the student safely and returns to guest mode."""
    session.clear()
    flash("You have been signed out safely.", "info")
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    """Displays registered student profile, persistent learning statistics, and account details."""
    user, user_id, _, _ = get_session_context()
    stats = get_assessment_stats(user_id=user_id)
    recent = get_all_assessments(limit=5, user_id=user_id)
    return render_template("account.html", current_user=user, stats=stats, recent=recent)


# --------------------------------------------------
# Routes: Personalized 7-Day Study Plan
# --------------------------------------------------

@app.route("/study-plan")
@app.route("/study-plan/<subject_id>")
def study_plan_view(subject_id=None):
    """
    Displays the personalized 7-day study plan generated from assessment gaps,
    complete with daily tasks, recommended resources, and interactive progress tracking.
    """
    user, user_id, guest_session_id, is_guest = get_session_context()

    plan_record = get_latest_study_plan(subject_id=subject_id, user_id=user_id, guest_session_id=guest_session_id)

    if not plan_record:
        latest_assessment = get_latest_assessment(user_id=user_id, guest_session_id=guest_session_id)
        if latest_assessment:
            target_sub = latest_assessment["subject_id"] if not subject_id else subject_id
            target_sub_obj = get_subject(target_sub) or {"name": target_sub.title()}
            rec_res = get_recommended_resources_for_assessment(latest_assessment, limit=4)
            plan_data = generate_seven_day_study_plan(
                subject_id=target_sub,
                subject_name=target_sub_obj.get("name", target_sub),
                score=latest_assessment["score"],
                total=latest_assessment["total"],
                weak_topics=latest_assessment["weak_topics"],
                topic_results=latest_assessment["topic_results"],
                recommended_resources=rec_res
            )
            plan_id = save_study_plan(
                subject_id=target_sub,
                subject_name=target_sub_obj.get("name", target_sub),
                plan_data=plan_data,
                assessment_id=latest_assessment["id"],
                user_id=user_id,
                guest_session_id=guest_session_id
            )
            plan_record = get_study_plan_by_id(plan_id)
        else:
            sub = get_subject(subject_id or "python") or get_subject("python")
            plan_data = generate_seven_day_study_plan(
                subject_id=sub["id"],
                subject_name=sub["name"],
                score=0,
                total=10,
                weak_topics=[],
                topic_results=[]
            )
            plan_id = save_study_plan(
                subject_id=sub["id"],
                subject_name=sub["name"],
                plan_data=plan_data,
                user_id=user_id,
                guest_session_id=guest_session_id
            )
            plan_record = get_study_plan_by_id(plan_id)

    plan_data = plan_record.get("plan", {})
    plan_data["id"] = plan_record["id"]
    plan_data["subject_name"] = plan_record["subject_name"]
    plan_data["created_at"] = plan_record.get("created_at")
    completed_tasks = [str(t) for t in plan_record.get("tasks_completed", [])]

    return render_template(
        "study_plan.html",
        plan=plan_data,
        completed_tasks=completed_tasks
    )


@app.route("/api/study-plan/toggle", methods=["POST"])
def toggle_study_plan_task():
    """Toggles completion status of a day's study activity."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    data = request.get_json() or {}
    plan_id = data.get("plan_id")
    day_num = data.get("day")
    is_completed = data.get("completed", True)

    if not plan_id or day_num is None:
        return jsonify({"status": "error", "message": "Missing plan_id or day"}), 400

    try:
        plan_id = int(plan_id)
        day_str = str(day_num)
        plan_record = get_study_plan_by_id(plan_id)
        if not plan_record:
            return jsonify({"status": "error", "message": "Plan not found"}), 404

        current_completed = [str(t) for t in plan_record.get("tasks_completed", [])]
        if is_completed and day_str not in current_completed:
            current_completed.append(day_str)
        elif not is_completed and day_str in current_completed:
            current_completed.remove(day_str)

        update_study_plan_tasks(plan_id, current_completed, user_id=user_id, guest_session_id=guest_session_id)
        return jsonify({"status": "ok", "completed_tasks": current_completed})
    except Exception as err:
        safe_log(f"Error toggling study plan task: {err}", level="error")
        return jsonify({"status": "error", "message": str(err)}), 500


# --------------------------------------------------
# Routes: Assessment Submission & Diagnostic Results
# --------------------------------------------------

@app.route("/submit-quiz", methods=["POST"])
@app.route("/submit-quiz/<subject_id>", methods=["POST"])
def submit_quiz(subject_id=None):
    """
    Evaluates submitted answers, records individual question-by-question responses,
    computes overall and topic-wise gap scores, generates AI Study Coach guidance,
    persists 7-day study plan, and saves securely scoped to user or guest.
    """
    if not subject_id:
        subject_id = request.form.get("subject_id", "ml")

    subject = get_subject(subject_id)
    if not subject:
        return redirect(url_for("subjects"))

    questions = subject["questions"]
    total = len(questions)

    topic_scores = {topic: [0, 0] for topic in subject["topics"]}
    score = 0
    answers_detail = []

    for q in questions:
        topic = q["topic"]
        if topic not in topic_scores:
            topic_scores[topic] = [0, 0]

        topic_scores[topic][1] += 1

        user_answer = request.form.get(f"question_{q['id']}")
        is_correct = bool(user_answer and user_answer.strip() == q["answer"].strip())
        if is_correct:
            score += 1
            topic_scores[topic][0] += 1

        answers_detail.append({
            "question_id": q["id"],
            "question": q["question"],
            "topic": topic,
            "options": q.get("options", []),
            "user_answer": user_answer.strip() if user_answer else None,
            "correct_answer": q["answer"].strip(),
            "is_correct": is_correct,
            "explanation": q.get("explanation", "")
        })

    overall_percentage = int((score / total) * 100) if total > 0 else 0

    topic_results = []
    weak_topics = []
    strong_topics = []

    for topic, (correct, count) in topic_scores.items():
        pct = int((correct / count) * 100) if count > 0 else 0

        if pct >= 70:
            status = "Strong"
            strong_topics.append(topic)
        elif pct >= 50:
            status = "Needs Improvement"
            weak_topics.append(f"{topic} ({pct}%)")
        else:
            status = "Weak"
            weak_topics.append(f"{topic} ({pct}%)")

        topic_results.append({
            "topic": topic,
            "correct": correct,
            "total": count,
            "score": pct,
            "status": status
        })

    sorted_topics = sorted(topic_results, key=lambda x: x["score"], reverse=True)
    strongest_topic = sorted_topics[0]["topic"] if sorted_topics and sorted_topics[0]["score"] >= 50 else None
    weakest_topic = sorted_topics[-1]["topic"] if sorted_topics and sorted_topics[-1]["score"] < 70 else None

    # ML Learning Pattern Analysis (K-Means clustering on topic performance)
    ml_analysis = None
    if analyze_topic_learning_patterns:
        try:
            ml_analysis = analyze_topic_learning_patterns(topic_results)
        except Exception as ml_err:
            safe_log(f"[ML Model] Error during topic clustering in submit_quiz: {ml_err}", level="warning")
            ml_analysis = None

    temp_assessment = {
        "subject_id": subject["id"],
        "subject_name": subject["name"],
        "topic_results": topic_results
    }
    recommended_resources = get_recommended_resources_for_assessment(temp_assessment, limit=4)

    # AI Study Coach Guidance with complete error isolation
    try:
        ai_coach = get_ai_coach_guidance(
            subject_name=subject["name"],
            score=score,
            total=total,
            topic_results=topic_results,
            weak_topics=weak_topics,
            strong_topics=strong_topics,
            strongest_topic=strongest_topic,
            weakest_topic=weakest_topic,
            recommended_resources=recommended_resources,
            ml_analysis=ml_analysis
        )
    except Exception as ai_err:
        safe_log(f"[AI Coach] Guidance generation error in submit_quiz: {ai_err}", level="warning")
        try:
            offline_md = generate_offline_study_guide(
                subject_name=subject["name"],
                score=score,
                total=total,
                weak_topics=weak_topics
            )
            ai_coach = markdown.markdown(offline_md, extensions=["extra", "nl2br"])
        except Exception:
            ai_coach = f"<p>Great effort on the {subject['name']} assessment ({score}/{total}). Review your topic performance breakdown below.</p>"

    # Retrieve current user or guest context
    user, user_id, guest_session_id, is_guest = get_session_context()

    # Save to SQLite database including answers_detail and ownership
    new_id = None
    try:
        new_id = save_assessment(
            subject_id=subject["id"],
            subject_name=subject["name"],
            score=score,
            total=total,
            percentage=overall_percentage,
            strongest_topic=strongest_topic or "None",
            weakest_topic=weakest_topic or "None",
            weak_topics=weak_topics,
            topic_results=topic_results,
            ai_coach_text=ai_coach,
            user_id=user_id,
            guest_session_id=guest_session_id,
            answers_detail=answers_detail
        )
    except Exception as db_err:
        safe_log(f"[Database Error] Could not save assessment: {db_err}", level="error")

    # Generate and save personalized 7-day study plan
    try:
        study_plan_data = generate_seven_day_study_plan(
            subject_id=subject["id"],
            subject_name=subject["name"],
            score=score,
            total=total,
            weak_topics=weak_topics,
            topic_results=topic_results,
            recommended_resources=recommended_resources
        )
        save_study_plan(
            subject_id=subject["id"],
            subject_name=subject["name"],
            plan_data=study_plan_data,
            assessment_id=new_id,
            user_id=user_id,
            guest_session_id=guest_session_id
        )
    except Exception as sp_err:
        safe_log(f"[Study Plan Error] Could not save initial study plan: {sp_err}", level="warning")

    if new_id and not app.config.get("TESTING"):
        return redirect(url_for("results_detail", assessment_id=new_id))

    return render_template(
        "results.html",
        assessment_id=new_id,
        subject=subject,
        subject_id=subject["id"],
        subject_name=subject["name"],
        score=score,
        total=total,
        percentage=overall_percentage,
        topic_results=topic_results,
        strongest_topic=strongest_topic,
        weakest_topic=weakest_topic,
        weak_topics=weak_topics,
        ai_coach=ai_coach,
        recommended_resources=recommended_resources,
        answers=answers_detail,
        is_guest=is_guest,
        ml_analysis=ml_analysis
    )


@app.route("/results/<int:assessment_id>")
def results_detail(assessment_id):
    """
    Renders past assessment results from SQLite with question review and ownership verification,
    preventing duplicate entries, unauthorized access, and redundant Gemini calls.
    """
    user, user_id, guest_session_id, is_guest = get_session_context()
    assessment = get_assessment_by_id(assessment_id)
    if not assessment:
        return redirect(url_for("progress"))

    # Verify authorization
    if not verify_assessment_ownership(assessment, user_id=user_id, guest_session_id=guest_session_id):
        if assessment.get("user_id") is not None and assessment.get("user_id") != user_id:
            flash("You do not have permission to view another student's private assessment results.", "warning")
            return redirect(url_for("progress"))

    subject = get_subject(assessment["subject_id"])
    recommended_resources = get_recommended_resources_for_assessment(assessment, limit=4)
    answers = assessment.get("answers") or []

    # ML Learning Pattern Analysis (K-Means clustering on topic performance)
    ml_analysis = None
    if analyze_topic_learning_patterns:
        try:
            ml_analysis = analyze_topic_learning_patterns(assessment.get("topic_results") or [])
        except Exception as ml_err:
            safe_log(f"[ML Model] Error during topic clustering in results_detail: {ml_err}", level="warning")
            ml_analysis = None

    return render_template(
        "results.html",
        assessment_id=assessment_id,
        subject=subject,
        subject_id=assessment["subject_id"],
        subject_name=assessment["subject_name"],
        score=assessment["score"],
        total=assessment["total"],
        percentage=assessment["percentage"],
        topic_results=assessment["topic_results"],
        strongest_topic=assessment["strongest_topic"] if assessment["strongest_topic"] != "None" else None,
        weakest_topic=assessment["weakest_topic"] if assessment["weakest_topic"] != "None" else None,
        weak_topics=assessment["weak_topics"],
        ai_coach=assessment.get("ai_coach_text") or "Detailed study guide stored with assessment.",
        recommended_resources=recommended_resources,
        answers=answers,
        is_guest=(user is None),
        ml_analysis=ml_analysis
    )


# --------------------------------------------------
# Routes: Learning Resources
# --------------------------------------------------

@app.route("/resources")
def resources_view():
    """
    Curated Learning Resources hub with interactive filters, search,
    and personalized recommendations based on the student's actual gaps.
    """
    user, user_id, guest_session_id, is_guest = get_session_context()
    subject_id = request.args.get("subject", "all").strip().lower()
    topic = request.args.get("topic", "all").strip()
    resource_type = request.args.get("type", "all").strip()
    difficulty = request.args.get("difficulty", "all").strip()
    access_type = request.args.get("access", "all").strip()
    search_query = request.args.get("q", "").strip()

    filtered_list = filter_resources(
        subject_id=subject_id if subject_id != "all" else None,
        topic=topic if topic != "all" else None,
        resource_type=resource_type if resource_type != "all" else None,
        difficulty=difficulty if difficulty != "all" else None,
        access_type=access_type if access_type != "all" else None,
        search_query=search_query
    )

    latest_per_subject = get_latest_assessments_by_subject(user_id=user_id, guest_session_id=guest_session_id)
    latest_assessment = None

    if subject_id != "all" and subject_id in latest_per_subject:
        latest_assessment = latest_per_subject[subject_id]
    else:
        latest_assessment = get_latest_assessment(user_id=user_id, guest_session_id=guest_session_id)

    recommended_resources = get_recommended_resources_for_assessment(latest_assessment, limit=6)
    bookmarked_ids = get_all_bookmarks(user_id=user_id, guest_session_id=guest_session_id)

    subjects_map = get_subjects_and_topics_map()
    available_topics = []
    if subject_id != "all" and subject_id in subjects_map:
        available_topics = subjects_map[subject_id]["topics"]
    else:
        for s_data in subjects_map.values():
            for t in s_data["topics"]:
                if t not in available_topics:
                    available_topics.append(t)

    return render_template(
        "resources.html",
        resources=filtered_list,
        recommended_resources=recommended_resources,
        latest_assessment=latest_assessment,
        subjects_map=subjects_map,
        available_topics=available_topics,
        bookmarked_ids=bookmarked_ids,
        active_filters={
            "subject": subject_id,
            "topic": topic,
            "type": resource_type,
            "difficulty": difficulty,
            "access": access_type,
            "q": search_query
        }
    )


@app.route("/resources/<subject_id>")
def resources_by_subject(subject_id):
    """Direct route for subject-specific learning resources."""
    return redirect(url_for("resources_view", subject=subject_id))


@app.route("/resources/<subject_id>/<topic>")
def resources_by_topic(subject_id, topic):
    """Direct route for topic-specific learning resources."""
    return redirect(url_for("resources_view", subject=subject_id, topic=topic))


@app.route("/api/bookmark", methods=["POST"])
def toggle_bookmark():
    """Toggles bookmark status for a resource in SQLite scoped to user or guest."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    data = request.get_json() or {}
    resource_id = data.get("resource_id")
    if not resource_id:
        return jsonify({"status": "error", "message": "Missing resource_id"}), 400

    bookmarks = get_all_bookmarks(user_id=user_id, guest_session_id=guest_session_id)
    if resource_id in bookmarks:
        remove_bookmark(resource_id, user_id=user_id, guest_session_id=guest_session_id)
        is_bookmarked = False
    else:
        add_bookmark(resource_id, user_id=user_id, guest_session_id=guest_session_id)
        is_bookmarked = True

    return jsonify({"status": "ok", "resource_id": resource_id, "bookmarked": is_bookmarked})


# --------------------------------------------------
# Routes: Progress & Analytics
# --------------------------------------------------

@app.route("/progress")
def progress():
    """Displays student assessment history and cross-subject progress tracking scoped to current user or guest."""
    user, user_id, guest_session_id, is_guest = get_session_context()
    analytics = get_dashboard_analytics(user_id=user_id, guest_session_id=guest_session_id)
    stats = analytics["raw_stats"]
    history = get_all_assessments(limit=50, user_id=user_id, guest_session_id=guest_session_id)
    all_subjects = analytics["subjects"]

    chronological = list(reversed(history[:10]))
    chart_points = [
        {
            "id": h["id"],
            "subject": h["subject_name"],
            "pct": h["percentage"],
            "score_str": f"{h['score']}/{h['total']}",
            "date": h["created_at"]
        }
        for h in chronological
    ]

    return render_template(
        "progress.html",
        stats=stats,
        analytics=analytics,
        history=history,
        subjects=all_subjects,
        chart_points=chart_points,
        is_guest=is_guest
    )


@app.route("/progress/clear", methods=["POST"])
def clear_progress():
    """Allows student to clear assessment history."""
    clear_history()
    return redirect(url_for("progress"))


@app.route("/how-it-works")
def how_it_works():
    """Direct route for How It Works."""
    return redirect(url_for("home", _anchor="how-it-works"))


@app.route("/about")
def about():
    """Direct route for About."""
    return redirect(url_for("home", _anchor="about"))


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    safe_log(f"LearnGap Server running on http://127.0.0.1:{port}")
    app.run(
        host="127.0.0.1",
        debug=True,
        port=port
    )
