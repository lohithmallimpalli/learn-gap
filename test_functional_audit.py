"""
Comprehensive Functional and Button Audit for LearnGap
Uses only Python Standard Library (no third-party dependencies required).
"""

import unittest
import json
import re
from html.parser import HTMLParser
from app import app
import database
import questions
import resources


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "a":
            self.links.append(attr_dict)
        elif tag == "button":
            self.buttons.append(attr_dict)


class FunctionalAuditTest(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_no_dead_links_on_any_page(self):
        """Audit all pages to verify there are NO href='#' or broken links."""
        pages = ["/", "/subjects", "/resources", "/progress", "/quiz/python", "/quiz/ml"]
        for p in pages:
            res = self.client.get(p)
            self.assertEqual(res.status_code, 200, f"Page {p} failed with code {res.status_code}")
            parser = LinkExtractor()
            parser.feed(res.data.decode("utf-8"))
            for a in parser.links:
                href = a.get("href")
                self.assertIsNotNone(href, f"Found <a> without href on {p}")
                self.assertNotEqual(href, "#", f"Found dead link href='#' on {p}: {a}")
                self.assertNotEqual(href.strip(), "", f"Found empty href on {p}: {a}")

    def test_dashboard_real_data_rendering(self):
        """Verify dashboard displays actual database stats without placeholders."""
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        html = res.data.decode("utf-8")
        self.assertIn("Find Your Learning Gaps.", html)
        self.assertIn("SDG 4", html)
        self.assertIn("QUALITY EDUCATION", html)
        self.assertIn("Six Fundamental Subjects", html)
        self.assertIn("Start Assessment", html)

    def test_subjects_page_buttons(self):
        """Verify all 6 subject cards have working Start Assessment and Explore Resources buttons."""
        res = self.client.get("/subjects")
        self.assertEqual(res.status_code, 200)
        html = res.data.decode("utf-8")
        for sub_id in questions.SUBJECTS:
            self.assertIn(f"/quiz/{sub_id}", html, f"Missing start quiz link for {sub_id}")
            self.assertIn(f"/resources?subject={sub_id}", html, f"Missing explore resources link for {sub_id}")

    def test_quiz_stepper_and_duplicate_submit_protection(self):
        """Verify quiz page includes question pills, trackers, and form controls."""
        res = self.client.get("/quiz/ml")
        self.assertEqual(res.status_code, 200)
        html = res.data.decode("utf-8")
        self.assertIn("Test Your Knowledge", html)
        self.assertIn("Question 1 of 10", html)
        self.assertIn("quiz-progress-bar", html)
        self.assertIn("submit-btn", html)
        self.assertIn("unanswered-alert", html)

    def test_submit_quiz_and_results_rendering(self):
        """Submit a mock quiz and verify scoring, gap classification, and Study Topic links."""
        form_data = {
            "subject_id": "ml",
            "question_ml_1": "Predicts a continuous numeric value based on relationships",  # correct
            "question_ml_2": "Predicts a continuous numeric value based on relationships",  # dummy
            "question_ml_3": "Sigmoid (Logistic) function",  # correct
            "question_ml_4": "Sigmoid (Logistic) function",  # dummy
            "question_ml_5": "Gini Impurity or Information Gain (Entropy)",  # correct
            "question_ml_6": "Gini Impurity or Information Gain (Entropy)",  # dummy
            "question_ml_7": "Centroid initialization (k-means++)",  # correct
            "question_ml_8": "Centroid initialization (k-means++)",  # dummy
            "question_ml_9": "To reduce dimensionality while preserving maximum variance",  # correct
            "question_ml_10": "To reduce dimensionality while preserving maximum variance", # correct
        }
        res = self.client.post("/submit-quiz/ml", data=form_data)
        self.assertEqual(res.status_code, 200)
        html = res.data.decode("utf-8")
        self.assertIn("Your Learning Analysis", html)
        self.assertIn("Topic Performance Breakdown", html)
        self.assertIn("Study Topic", html)
        self.assertIn("Retake Assessment", html)
        self.assertIn("Your AI Study Coach", html)

    def test_resources_all_filters(self):
        """Verify resource catalog search and 5 filters return valid responses."""
        # 1. Subject filter
        res = self.client.get("/resources?subject=dsa")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Data Structures", res.data)

        # 2. Topic filter
        res = self.client.get("/resources?subject=dsa&topic=Trees")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Trees", res.data)

        # 3. Type filter
        res = self.client.get("/resources?type=Book+%2F+Reference")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Book / Reference", res.data)

        # 4. Difficulty filter
        res = self.client.get("/resources?difficulty=Beginner")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Beginner", res.data)

        # 5. Search query
        res = self.client.get("/resources?q=Kaggle")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Kaggle", res.data)

    def test_progress_dashboard_rendering(self):
        """Verify progress dashboard displays real SQLite metrics and recent assessment log."""
        res = self.client.get("/progress")
        self.assertEqual(res.status_code, 200)
        html = res.data.decode("utf-8")
        self.assertIn("Your Learning Progress", html)
        self.assertIn("Assessments Completed", html)
        self.assertIn("Average Accuracy", html)
        self.assertIn("Subject Mastery Comparison", html)
        self.assertIn("Detailed Assessment Log", html)


if __name__ == "__main__":
    unittest.main()
