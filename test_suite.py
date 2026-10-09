"""
Automated Comprehensive Test Suite for LearnGap
Tests routes, scoring, topic analysis, resource recommendations, filters, and database safety.
"""

import unittest
import json
from app import app
import database
import questions
import resources
import knowledge_base


class LearnGapTestSuite(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    # --- Test 1: Core Navigation Routes ---
    def test_navigation_routes(self):
        routes = ["/", "/subjects", "/resources", "/progress"]
        for r in routes:
            response = self.client.get(r)
            self.assertEqual(response.status_code, 200, f"Route {r} failed with status {response.status_code}")

    # --- Test 2: All 6 Subject Quiz Routes ---
    def test_quiz_routes_all_subjects(self):
        for subject_id in questions.SUBJECTS:
            response = self.client.get(f"/quiz/{subject_id}")
            self.assertEqual(response.status_code, 200, f"Quiz route /quiz/{subject_id} failed")
            self.assertIn(b"Test Your Knowledge", response.data)

    # --- Test 3: Invalid Subject Redirects ---
    def test_invalid_subject_redirect(self):
        response = self.client.get("/quiz/invalid_subject_xyz")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/subjects", response.headers["Location"])

    # --- Test 4: Resource Catalogue Filters ---
    def test_resource_filters(self):
        # Filter by subject
        py_res = resources.filter_resources(subject_id="python")
        self.assertGreater(len(py_res), 0)
        for r in py_res:
            self.assertEqual(r["subject_id"], "python")

        # Filter by difficulty
        beg_res = resources.filter_resources(difficulty="Beginner")
        self.assertGreater(len(beg_res), 0)
        for r in beg_res:
            self.assertEqual(r["difficulty"], "Beginner")

        # Filter by access type
        free_res = resources.filter_resources(access_type="Free")
        self.assertGreater(len(free_res), 0)
        for r in free_res:
            self.assertIn("Free", r["access_type"])

        # Search query
        search_res = resources.filter_resources(search_query="K-Means")
        self.assertGreater(len(search_res), 0)

    # --- Test 5: Personalized Resource Recommendation Engine ---
    def test_personalized_recommendation_logic(self):
        mock_assessment = {
            "subject_id": "ml",
            "subject_name": "Machine Learning",
            "topic_results": [
                {"topic": "Linear Regression", "score": 100, "status": "Strong"},
                {"topic": "Logistic Regression", "score": 50, "status": "Needs Improvement"},
                {"topic": "Decision Tree", "score": 100, "status": "Strong"},
                {"topic": "K-Means", "score": 0, "status": "Weak"},
                {"topic": "PCA", "score": 100, "status": "Strong"}
            ]
        }
        recs = resources.get_recommended_resources_for_assessment(mock_assessment, limit=4)
        self.assertGreater(len(recs), 0)

        # First recommendation must be for K-Means (0% Weak)
        self.assertEqual(recs[0]["topic"], "K-Means")
        self.assertIn("K-Means", recs[0]["recommendation_reason"])
        self.assertEqual(recs[0]["priority_level"], "Critical Gap")

    # --- Test 6: SQLite Database Persistence ---
    def test_database_stats_and_persistence(self):
        stats = database.get_assessment_stats()
        self.assertIn("total_assessments", stats)
        self.assertIn("average_score", stats)
        self.assertIn("subjects_attempted", stats)
        self.assertGreater(stats["total_assessments"], 0)

    # --- Test 7: Bookmarks API ---
    def test_bookmarks_api(self):
        res_id = "test-bookmark-dsa-clrs"
        # Add bookmark
        add_resp = self.client.post("/api/bookmark", json={"resource_id": res_id})
        self.assertEqual(add_resp.status_code, 200)
        data = json.loads(add_resp.data)
        self.assertTrue(data["bookmarked"])

        # Toggle off
        rem_resp = self.client.post("/api/bookmark", json={"resource_id": res_id})
        self.assertEqual(rem_resp.status_code, 200)
        data2 = json.loads(rem_resp.data)
        self.assertFalse(data2["bookmarked"])

    # --- Test 8: Offline Study Guide Fallback ---
    def test_offline_knowledge_fallback(self):
        guide = knowledge_base.generate_offline_study_guide(
            subject_name="Operating Systems",
            score=6,
            total=10,
            weak_topics=["Deadlocks (0%)", "CPU Scheduling (50%)"]
        )
        self.assertIn("Deadlocks", guide)
        self.assertIn("CPU Scheduling", guide)
        self.assertIn("3 Important Concepts", guide)
        self.assertIn("2 Quick Hints", guide)


if __name__ == "__main__":
    unittest.main()
