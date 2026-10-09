"""
LearnGap Machine Learning Module: K-Means Topic Performance Pattern Analysis
=============================================================================

Technical Overview & Methodology:
---------------------------------
1. Why K-Means Clustering is Used:
   - LearnGap analyzes student assessment results at the granular topic level.
   - Traditional educational metrics rely on fixed, static cutoffs (e.g., 70% = pass).
   - K-Means is an unsupervised machine learning algorithm that groups data points
     into k distinct clusters by minimizing the within-cluster sum of squares
     (inertia) based on geometric distance to cluster centroids.
   - It is ideal for identifying relative performance tiers and natural groupings
     across topics without requiring pre-labeled training data or supervised labels.

2. Input Features:
   - The primary input feature vector is each topic's achieved accuracy percentage
     (0.0 to 100.0) from the submitted diagnostic assessment.
   - Formatted as a 2D numerical feature matrix X of shape (N, 1), where N is the
     number of distinct evaluated topics.

3. What the Clusters Represent:
   - Topic performance patterns are partitioned into relative learning tiers:
     * 'Strong Performance': Topics clustered near the highest score centroid,
       demonstrating high conceptual confidence on this assessment.
     * 'Developing': Topics clustered near the intermediate centroid, indicating
       a foundational working grasp that needs reinforcement.
     * 'Priority for Improvement': Topics clustered near the lower centroid,
       representing relative learning gaps that warrant prioritized study.

4. Exploratory Learning-Pattern Analysis (Important Scope & Ethics):
   - This clustering is strictly an exploratory learning-pattern analysis.
   - It does NOT medically, psychologically, or definitively diagnose a student's
     innate cognitive capability.
   - It provides an adaptive, data-driven snapshot of relative topic strengths
     and gaps for this specific assessment attempt.

5. Relationship to Assessment Scoring Rules:
   - Clustering does NOT replace the factual assessment scoring rules or the
     question-level correctness logic.
   - It complements the diagnostic rubric by structuring topics into actionable
     tiers for both the student UI and the Gemini AI Study Coach.
"""

import logging
from typing import Any, Dict, List, Optional
import numpy as np
from sklearn.cluster import KMeans

logger = logging.getLogger(__name__)

# Standard UI and context explanation
EXPLANATION_TEXT = (
    "LearnGap uses K-Means clustering to group topic-level performance into "
    "learning patterns and identify areas that may need additional attention."
)

# Standard performance tiers
TIER_STRONG = "Strong Performance"
TIER_DEVELOPING = "Developing"
TIER_PRIORITY = "Priority for Improvement"


def _create_empty_result(status: str = "insufficient_data", message: str = "") -> Dict[str, Any]:
    """Returns a safe, standardized structure when input data cannot be clustered."""
    return {
        "status": status,
        "message": message or "Insufficient topic data for ML pattern analysis.",
        "groups": [
            {
                "name": TIER_STRONG,
                "key": "strong",
                "topics": [],
                "badge_class": "badge-green",
                "border_color": "var(--success, #059669)",
                "count": 0
            },
            {
                "name": TIER_DEVELOPING,
                "key": "developing",
                "topics": [],
                "badge_class": "badge-amber",
                "border_color": "var(--warning, #D97706)",
                "count": 0
            },
            {
                "name": TIER_PRIORITY,
                "key": "priority",
                "topics": [],
                "badge_class": "badge-red",
                "border_color": "var(--danger, #DC2626)",
                "count": 0
            }
        ],
        "clusters": {
            TIER_STRONG: [],
            TIER_DEVELOPING: [],
            TIER_PRIORITY: []
        },
        "formatted_summary": "",
        "explanation": EXPLANATION_TEXT,
        "k_used": 0,
        "total_topics": 0
    }


def analyze_topic_learning_patterns(topic_scores: Optional[List[Dict[str, Any]]]) -> Dict[str, Any]:
    """
    Executes K-Means clustering on topic-level assessment scores to identify
    learning-performance groups (Strong Performance, Developing, Priority for Improvement).

    Accepts topic-level score lists such as:
    [
        {"topic": "Linear Regression", "score": 50},
        {"topic": "Logistic Regression", "score": 80},
        {"topic": "Decision Tree", "score": 70},
        {"topic": "K-Means", "score": 40},
        {"topic": "PCA", "score": 90}
    ]

    Robustness Guarantees:
    - Safely handles missing scores, non-numeric values, or None inputs
    - Handles fewer than 3 topics gracefully
    - Handles duplicate scores and uniform scores across all topics
    - Never raises uncaught exceptions or crashes calling workflows

    Returns:
        Dict containing status, grouped topics, cluster mappings, formatted AI prompt summary,
        and UI metadata.
    """
    try:
        # 1. Validate container type
        if not isinstance(topic_scores, (list, tuple)) or not topic_scores:
            return _create_empty_result(status="insufficient_data", message="No topic score records provided.")

        # 2. Extract and sanitize valid topic-score tuples
        cleaned_topics: List[Dict[str, Any]] = []
        for item in topic_scores:
            if not isinstance(item, dict):
                continue

            raw_topic = item.get("topic") or item.get("name")
            if not raw_topic:
                continue
            topic_str = str(raw_topic).strip()

            raw_score = item.get("score")
            if raw_score is None:
                continue

            try:
                numeric_score = float(raw_score)
                if np.isnan(numeric_score) or np.isinf(numeric_score):
                    continue
                # Constrain to valid percentage range [0.0, 100.0]
                clamped_score = max(0.0, min(100.0, numeric_score))
                cleaned_topics.append({
                    "topic": topic_str,
                    "score": clamped_score
                })
            except (ValueError, TypeError):
                # Safely ignore non-numeric scores
                continue

        # 3. Check if we have sufficient sanitized samples
        n_samples = len(cleaned_topics)
        if n_samples == 0:
            return _create_empty_result(status="insufficient_data", message="No valid numeric topic scores found.")

        # Build feature matrix X of shape (n_samples, 1)
        X = np.array([[t["score"]] for t in cleaned_topics], dtype=float)
        unique_scores = np.unique(X)
        n_unique = len(unique_scores)

        # 4. Adaptive selection of k (number of clusters)
        # Cannot have more clusters than distinct data points or total samples
        k = min(3, n_samples, n_unique)

        # Mapping: cluster_label (int) -> group_name (str)
        group_map: Dict[int, str] = {}
        km_labels: List[int] = []

        if k <= 1:
            # Case A: Uniform scores or single topic (0 variance)
            # Assign uniform group based on average performance level
            avg_score = float(np.mean(X))
            if avg_score >= 70.0:
                tier = TIER_STRONG
            elif avg_score >= 50.0:
                tier = TIER_DEVELOPING
            else:
                tier = TIER_PRIORITY

            km_labels = [0] * n_samples
            group_map = {0: tier}

        elif k == 2:
            # Case B: Exactly 2 distinct score tiers or 2 samples
            kmeans_model = KMeans(n_clusters=2, random_state=42, n_init=10)
            kmeans_model.fit(X)
            km_labels = list(kmeans_model.labels_)
            centers = kmeans_model.cluster_centers_.flatten()

            # Sort cluster indices by centroid: low_idx has smaller centroid, high_idx has larger
            sorted_indices = sorted(range(2), key=lambda i: centers[i])
            low_idx, high_idx = sorted_indices[0], sorted_indices[1]
            c_low, c_high = centers[low_idx], centers[high_idx]

            # Categorize the two clusters based on their relative and absolute centers
            if c_high >= 70.0:
                high_tier = TIER_STRONG
                low_tier = TIER_PRIORITY if c_low < 50.0 else TIER_DEVELOPING
            else:
                high_tier = TIER_DEVELOPING
                low_tier = TIER_PRIORITY

            group_map = {high_idx: high_tier, low_idx: low_tier}

        else:
            # Case C: 3 or more distinct score tiers (standard K-Means clustering)
            kmeans_model = KMeans(n_clusters=3, random_state=42, n_init=10)
            kmeans_model.fit(X)
            km_labels = list(kmeans_model.labels_)
            centers = kmeans_model.cluster_centers_.flatten()

            # Sort cluster indices ascending: low -> mid -> high
            sorted_indices = sorted(range(3), key=lambda i: centers[i])
            low_idx = sorted_indices[0]
            mid_idx = sorted_indices[1]
            high_idx = sorted_indices[2]

            group_map = {
                high_idx: TIER_STRONG,
                mid_idx: TIER_DEVELOPING,
                low_idx: TIER_PRIORITY
            }

        # 5. Populate grouped topic containers
        grouped_topics: Dict[str, List[Dict[str, Any]]] = {
            TIER_STRONG: [],
            TIER_DEVELOPING: [],
            TIER_PRIORITY: []
        }

        for item, label in zip(cleaned_topics, km_labels):
            tier_name = group_map.get(label, TIER_DEVELOPING)
            grouped_topics[tier_name].append({
                "topic": item["topic"],
                "score": int(round(item["score"]))
            })

        # Sort topics within each group descending by score for clear presentation
        for tier_name in grouped_topics:
            grouped_topics[tier_name].sort(key=lambda x: x["score"], reverse=True)

        # 6. Format concise summary text for Gemini AI Study Coach context
        summary_lines = ["ML Learning Pattern:"]
        for tier_name in [TIER_STRONG, TIER_DEVELOPING, TIER_PRIORITY]:
            topic_names = [t["topic"] for t in grouped_topics[tier_name]]
            if topic_names:
                summary_lines.append(f"- {tier_name}: {', '.join(topic_names)}")

        formatted_summary = "\n".join(summary_lines)

        # 7. Construct final structured payload for UI and application
        groups_list = [
            {
                "name": TIER_STRONG,
                "key": "strong",
                "topics": grouped_topics[TIER_STRONG],
                "badge_class": "badge-green",
                "border_color": "var(--success, #059669)",
                "count": len(grouped_topics[TIER_STRONG])
            },
            {
                "name": TIER_DEVELOPING,
                "key": "developing",
                "topics": grouped_topics[TIER_DEVELOPING],
                "badge_class": "badge-amber",
                "border_color": "var(--warning, #D97706)",
                "count": len(grouped_topics[TIER_DEVELOPING])
            },
            {
                "name": TIER_PRIORITY,
                "key": "priority",
                "topics": grouped_topics[TIER_PRIORITY],
                "badge_class": "badge-red",
                "border_color": "var(--danger, #DC2626)",
                "count": len(grouped_topics[TIER_PRIORITY])
            }
        ]

        return {
            "status": "success",
            "groups": groups_list,
            "clusters": {tier: [t["topic"] for t in grouped_topics[tier]] for tier in grouped_topics},
            "formatted_summary": formatted_summary,
            "explanation": EXPLANATION_TEXT,
            "k_used": k,
            "total_topics": n_samples
        }

    except Exception as err:
        logger.warning("Graceful fallback triggered in analyze_topic_learning_patterns: %s", err)
        fallback = _create_empty_result(status="fallback", message=f"ML analysis error: {err}")
        return fallback
