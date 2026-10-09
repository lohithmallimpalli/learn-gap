import sqlite3
import os
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "learngap.db")


def get_db_connection():
    """Returns a SQLite connection with dict-like row access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes and safely migrates the SQLite database schema."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Registered Students / Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 2. Core assessments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id TEXT NOT NULL,
            subject_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage INTEGER NOT NULL,
            strongest_topic TEXT,
            weakest_topic TEXT,
            weak_topics_json TEXT,
            topic_results_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Safe migrations for assessments table
    existing_assessment_cols = [row["name"] for row in cursor.execute("PRAGMA table_info(assessments)").fetchall()]
    
    if "ai_coach_text" not in existing_assessment_cols:
        cursor.execute("ALTER TABLE assessments ADD COLUMN ai_coach_text TEXT")
    if "user_id" not in existing_assessment_cols:
        cursor.execute("ALTER TABLE assessments ADD COLUMN user_id INTEGER")
    if "guest_session_id" not in existing_assessment_cols:
        cursor.execute("ALTER TABLE assessments ADD COLUMN guest_session_id TEXT")
    if "answers_json" not in existing_assessment_cols:
        cursor.execute("ALTER TABLE assessments ADD COLUMN answers_json TEXT")

    # 3. 7-Day Personalized Study Plans table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_session_id TEXT,
            assessment_id INTEGER,
            subject_id TEXT NOT NULL,
            subject_name TEXT NOT NULL,
            plan_json TEXT NOT NULL,
            tasks_completed_json TEXT DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 4. Bookmarks table for saving preferred learning resources
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_id TEXT NOT NULL,
            user_id INTEGER,
            guest_session_id TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Safe migration for bookmarks table
    existing_bookmark_cols = [row["name"] for row in cursor.execute("PRAGMA table_info(bookmarks)").fetchall()]
    if "user_id" not in existing_bookmark_cols:
        cursor.execute("ALTER TABLE bookmarks ADD COLUMN user_id INTEGER")
    if "guest_session_id" not in existing_bookmark_cols:
        cursor.execute("ALTER TABLE bookmarks ADD COLUMN guest_session_id TEXT")

    conn.commit()
    conn.close()


# --------------------------------------------------------------------------
# User Account Operations
# --------------------------------------------------------------------------

def create_user(arg1=None, arg2=None, arg3=None, name=None, email=None, password_hash=None):
    """
    Creates a new registered student account.
    Accepts create_user(name, email, password_hash),
    create_user(email, password_hash, name),
    or keyword arguments create_user(email=..., password_hash=..., name=...).
    """
    pos_args = [a for a in (arg1, arg2, arg3) if a is not None]
    if pos_args:
        for a in list(pos_args):
            if isinstance(a, str) and "@" in a and not email:
                email = a
                pos_args.remove(a)
                break
        for a in list(pos_args):
            if isinstance(a, str) and (len(a) > 25 or ":" in a or "hash" in a) and not password_hash:
                password_hash = a
                pos_args.remove(a)
                break
        if pos_args and not name:
            name = pos_args[0]

    name = (name or "Student").strip()
    email = (email or "").strip().lower()
    password_hash = password_hash or ""

    if not email or not password_hash:
        return None

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (name, email, password_hash, created_at)
            VALUES (?, ?, ?, datetime('now', 'localtime'))
        """, (name, email, password_hash))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return get_user_by_id(user_id)
    except sqlite3.IntegrityError:
        conn.close()
        return None


def get_user_by_email(email):
    """Fetches user record by email (case-insensitive)."""
    if not email:
        return None
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE LOWER(email) = LOWER(?)", (email.strip(),))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def get_user_by_id(user_id):
    """Fetches user record by ID."""
    if not user_id:
        return None
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


# --------------------------------------------------------------------------
# Assessment Operations (Scoped & Unscoped)
# --------------------------------------------------------------------------

def save_assessment(subject_id, subject_name, score, total, percentage,
                    strongest_topic, weakest_topic, weak_topics, topic_results,
                    ai_coach_text="", user_id=None, guest_session_id=None, answers=None, answers_detail=None):
    """Saves a completed assessment record to SQLite with user/guest ownership."""
    if answers is None and answers_detail is not None:
        answers = answers_detail
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO assessments (
            subject_id, subject_name, score, total, percentage,
            strongest_topic, weakest_topic, weak_topics_json, topic_results_json,
            ai_coach_text, user_id, guest_session_id, answers_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))
    """, (
        subject_id,
        subject_name,
        score,
        total,
        percentage,
        strongest_topic,
        weakest_topic,
        json.dumps(weak_topics),
        json.dumps(topic_results),
        ai_coach_text,
        user_id,
        guest_session_id,
        json.dumps(answers or [])
    ))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def _parse_assessment_row(r):
    """Helper to convert a SQLite Row to a dictionary with parsed JSON fields."""
    if not r:
        return None
    item = dict(r)
    try:
        item["weak_topics"] = json.loads(item.get("weak_topics_json") or "[]")
    except Exception:
        item["weak_topics"] = []
    try:
        item["topic_results"] = json.loads(item.get("topic_results_json") or "[]")
    except Exception:
        item["topic_results"] = []
    try:
        item["answers"] = json.loads(item.get("answers_json") or "[]")
    except Exception:
        item["answers"] = []
    return item


def get_assessment_by_id(assessment_id):
    """Retrieves a single assessment by its database ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assessments WHERE id = ?", (assessment_id,))
    row = cursor.fetchone()
    conn.close()
    return _parse_assessment_row(row) if row else None


def verify_assessment_ownership(assessment, user_id=None, guest_session_id=None):
    """
    Validates whether the current student or guest owns the given assessment.
    Prevents unauthorized access via ID manipulation.
    """
    if isinstance(assessment, (int, str)):
        try:
            assessment = get_assessment_by_id(int(assessment))
        except Exception:
            return False
    if not assessment:
        return False
    rec_user_id = assessment.get("user_id")
    rec_guest_id = assessment.get("guest_session_id")

    # If associated with a registered user
    if rec_user_id is not None:
        return user_id is not None and int(rec_user_id) == int(user_id)

    # If associated with a guest session
    if rec_guest_id:
        return guest_session_id is not None and rec_guest_id == guest_session_id

    # Legacy assessment without ownership assigned: allow viewing
    return True


def get_latest_assessment(user_id=None, guest_session_id=None):
    """Retrieves the most recent assessment scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if user_id is not None:
        cursor.execute("SELECT * FROM assessments WHERE user_id = ? ORDER BY id DESC LIMIT 1", (user_id,))
    elif guest_session_id is not None:
        cursor.execute("SELECT * FROM assessments WHERE guest_session_id = ? ORDER BY id DESC LIMIT 1", (guest_session_id,))
    else:
        cursor.execute("SELECT * FROM assessments ORDER BY id DESC LIMIT 1")

    row = cursor.fetchone()
    conn.close()
    return _parse_assessment_row(row) if row else None


def get_latest_assessments_by_subject(user_id=None, guest_session_id=None):
    """
    Returns a dictionary of {subject_id: assessment_dict} representing the
    most recent attempt for each evaluated subject, scoped to user or guest.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    if user_id is not None:
        cursor.execute("""
            SELECT * FROM assessments
            WHERE user_id = ? AND id IN (
                SELECT MAX(id) FROM assessments WHERE user_id = ? GROUP BY subject_id
            )
            ORDER BY id DESC
        """, (user_id, user_id))
    elif guest_session_id is not None:
        cursor.execute("""
            SELECT * FROM assessments
            WHERE guest_session_id = ? AND id IN (
                SELECT MAX(id) FROM assessments WHERE guest_session_id = ? GROUP BY subject_id
            )
            ORDER BY id DESC
        """, (guest_session_id, guest_session_id))
    else:
        cursor.execute("""
            SELECT * FROM assessments
            WHERE id IN (
                SELECT MAX(id) FROM assessments GROUP BY subject_id
            )
            ORDER BY id DESC
        """)

    rows = cursor.fetchall()
    conn.close()
    return {r["subject_id"]: _parse_assessment_row(r) for r in rows}


def get_all_assessments(limit=50, user_id=None, guest_session_id=None):
    """Retrieves past assessments in descending order, scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if user_id is not None:
        cursor.execute("""
            SELECT * FROM assessments
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT ?
        """, (user_id, limit))
    elif guest_session_id is not None:
        cursor.execute("""
            SELECT * FROM assessments
            WHERE guest_session_id = ?
            ORDER BY id DESC
            LIMIT ?
        """, (guest_session_id, limit))
    else:
        cursor.execute("""
            SELECT * FROM assessments
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

    rows = cursor.fetchall()
    conn.close()
    return [_parse_assessment_row(r) for r in rows]


def get_assessment_stats(user_id=None, guest_session_id=None):
    """Computes high-level progress statistics scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()

    where_clause = ""
    params = []
    if user_id is not None:
        where_clause = "WHERE user_id = ?"
        params = [user_id]
    elif guest_session_id is not None:
        where_clause = "WHERE guest_session_id = ?"
        params = [guest_session_id]

    cursor.execute(f"SELECT COUNT(*) AS total_count, AVG(percentage) AS avg_pct FROM assessments {where_clause}", params)
    summary = cursor.fetchone()
    total_count = summary["total_count"] if summary else 0
    avg_pct = round(summary["avg_pct"], 1) if summary and summary["avg_pct"] is not None else 0

    cursor.execute(f"SELECT COUNT(DISTINCT subject_id) AS unique_subjects FROM assessments {where_clause}", params)
    sub_row = cursor.fetchone()
    unique_subjects = sub_row["unique_subjects"] if sub_row else 0

    # Best score per subject
    if user_id is not None:
        cursor.execute("""
            SELECT subject_id, subject_name, MAX(percentage) AS best_pct, COUNT(*) AS attempt_count,
                   MAX(created_at) AS last_attempt
            FROM assessments
            WHERE user_id = ?
            GROUP BY subject_id
        """, (user_id,))
    elif guest_session_id is not None:
        cursor.execute("""
            SELECT subject_id, subject_name, MAX(percentage) AS best_pct, COUNT(*) AS attempt_count,
                   MAX(created_at) AS last_attempt
            FROM assessments
            WHERE guest_session_id = ?
            GROUP BY subject_id
        """, (guest_session_id,))
    else:
        cursor.execute("""
            SELECT subject_id, subject_name, MAX(percentage) AS best_pct, COUNT(*) AS attempt_count,
                   MAX(created_at) AS last_attempt
            FROM assessments
            GROUP BY subject_id
        """)

    subject_stats = [dict(r) for r in cursor.fetchall()]
    conn.close()

    return {
        "total_assessments": total_count,
        "average_score": avg_pct,
        "subjects_attempted": unique_subjects,
        "subject_stats": subject_stats
    }


# --------------------------------------------------------------------------
# Guest-to-Account Conversion & Transfer
# --------------------------------------------------------------------------

def transfer_guest_data_to_user(guest_session_id, user_id):
    """
    Safely transfers assessments, study plans, and bookmarks generated during
    a guest session to a newly registered student account.
    Transfers ONLY records strictly matching the specific guest_session_id.
    """
    if not guest_session_id or not user_id:
        return 0

    conn = get_db_connection()
    cursor = conn.cursor()

    # Transfer assessments
    cursor.execute("""
        UPDATE assessments
        SET user_id = ?, guest_session_id = NULL
        WHERE guest_session_id = ? AND user_id IS NULL
    """, (user_id, guest_session_id))
    transferred_count = cursor.rowcount

    # Transfer study plans
    cursor.execute("""
        UPDATE study_plans
        SET user_id = ?, guest_session_id = NULL
        WHERE guest_session_id = ? AND user_id IS NULL
    """, (user_id, guest_session_id))

    # Transfer bookmarks
    cursor.execute("""
        UPDATE bookmarks
        SET user_id = ?, guest_session_id = NULL
        WHERE guest_session_id = ? AND user_id IS NULL
    """, (user_id, guest_session_id))

    conn.commit()
    conn.close()
    return transferred_count


# --------------------------------------------------------------------------
# Study Plan Operations
# --------------------------------------------------------------------------

def save_study_plan(subject_id, subject_name, plan_data, assessment_id=None,
                    user_id=None, guest_session_id=None):
    """Saves or updates a personalized 7-day study plan in SQLite."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO study_plans (
            user_id, guest_session_id, assessment_id, subject_id, subject_name,
            plan_json, tasks_completed_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, '[]', datetime('now', 'localtime'))
    """, (
        user_id,
        guest_session_id,
        assessment_id,
        subject_id,
        subject_name,
        json.dumps(plan_data)
    ))
    conn.commit()
    plan_id = cursor.lastrowid
    conn.close()
    return plan_id


def get_latest_study_plan(arg1=None, user_id=None, guest_session_id=None, subject_id=None):
    """Retrieves the latest 7-day study plan scoped to user or guest."""
    if arg1 is not None:
        if isinstance(arg1, int):
            user_id = user_id or arg1
        elif isinstance(arg1, str):
            subject_id = subject_id or arg1

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM study_plans WHERE "
    params = []

    if user_id is not None:
        query += "user_id = ? "
        params.append(user_id)
    elif guest_session_id is not None:
        query += "guest_session_id = ? "
        params.append(guest_session_id)
    else:
        query += "1=1 "

    if subject_id:
        query += "AND subject_id = ? "
        params.append(subject_id)

    query += "ORDER BY id DESC LIMIT 1"

    cursor.execute(query, params)
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    item = dict(row)
    try:
        item["plan"] = json.loads(item.get("plan_json") or "{}")
    except Exception:
        item["plan"] = {}
    try:
        item["tasks_completed"] = json.loads(item.get("tasks_completed_json") or "[]")
    except Exception:
        item["tasks_completed"] = []
    return item


def get_study_plan_by_id(plan_id):
    """Retrieves a study plan by its database ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM study_plans WHERE id = ?", (plan_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    item = dict(row)
    try:
        item["plan"] = json.loads(item.get("plan_json") or "{}")
    except Exception:
        item["plan"] = {}
    try:
        item["tasks_completed"] = json.loads(item.get("tasks_completed_json") or "[]")
    except Exception:
        item["tasks_completed"] = []
    return item


def update_study_plan_tasks(plan_id, tasks_completed, user_id=None, guest_session_id=None):
    """Updates the completed tasks checklist for an active study plan."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Validate ownership before update
    if user_id is not None:
        cursor.execute("SELECT id FROM study_plans WHERE id = ? AND user_id = ?", (plan_id, user_id))
    elif guest_session_id is not None:
        cursor.execute("SELECT id FROM study_plans WHERE id = ? AND guest_session_id = ?", (plan_id, guest_session_id))
    else:
        cursor.execute("SELECT id FROM study_plans WHERE id = ?", (plan_id,))

    if not cursor.fetchone():
        conn.close()
        return False

    cursor.execute("""
        UPDATE study_plans
        SET tasks_completed_json = ?
        WHERE id = ?
    """, (json.dumps(tasks_completed), plan_id))
    conn.commit()
    conn.close()
    return True


# --------------------------------------------------------------------------
# Bookmarks Operations
# --------------------------------------------------------------------------

def add_bookmark(resource_id, user_id=None, guest_session_id=None):
    """Saves a resource bookmark to SQLite scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO bookmarks (resource_id, user_id, guest_session_id, created_at)
            VALUES (?, ?, ?, datetime('now', 'localtime'))
        """, (resource_id, user_id, guest_session_id))
        conn.commit()
        success = True
    except Exception:
        success = False
    conn.close()
    return success


def remove_bookmark(resource_id, user_id=None, guest_session_id=None):
    """Removes a resource bookmark from SQLite scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id is not None:
        cursor.execute("DELETE FROM bookmarks WHERE resource_id = ? AND user_id = ?", (resource_id, user_id))
    elif guest_session_id is not None:
        cursor.execute("DELETE FROM bookmarks WHERE resource_id = ? AND guest_session_id = ?", (resource_id, guest_session_id))
    else:
        cursor.execute("DELETE FROM bookmarks WHERE resource_id = ?", (resource_id,))
    conn.commit()
    conn.close()
    return True


def get_all_bookmarks(user_id=None, guest_session_id=None):
    """Returns a set of bookmarked resource IDs scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id is not None:
        cursor.execute("SELECT resource_id FROM bookmarks WHERE user_id = ?", (user_id,))
    elif guest_session_id is not None:
        cursor.execute("SELECT resource_id FROM bookmarks WHERE guest_session_id = ?", (guest_session_id,))
    else:
        cursor.execute("SELECT resource_id FROM bookmarks")
    rows = cursor.fetchall()
    conn.close()
    return set(r["resource_id"] for r in rows)


def clear_history(user_id=None, guest_session_id=None):
    """Clears stored assessment history strictly scoped to user or guest."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id is not None:
        cursor.execute("DELETE FROM assessments WHERE user_id = ?", (user_id,))
        cursor.execute("DELETE FROM study_plans WHERE user_id = ?", (user_id,))
        cursor.execute("DELETE FROM bookmarks WHERE user_id = ?", (user_id,))
    elif guest_session_id is not None:
        cursor.execute("DELETE FROM assessments WHERE guest_session_id = ?", (guest_session_id,))
        cursor.execute("DELETE FROM study_plans WHERE guest_session_id = ?", (guest_session_id,))
        cursor.execute("DELETE FROM bookmarks WHERE guest_session_id = ?", (guest_session_id,))
    else:
        # Legacy/admin clear
        cursor.execute("DELETE FROM assessments")
        cursor.execute("DELETE FROM study_plans")
        cursor.execute("DELETE FROM bookmarks")
    conn.commit()
    conn.close()


# Ensure DB schema is initialized and migrated
init_db()
