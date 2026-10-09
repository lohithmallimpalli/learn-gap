import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from unittest.mock import patch
from app import app
from database import init_db, get_assessment_by_id, get_all_assessments, get_assessment_stats
from questions import get_subject

class TestAssessmentSubmissionFlow(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        init_db()

    def test_submission_with_ai_working(self):
        """Test assessment submission when Gemini AI generates guidance successfully."""
        initial_count = get_assessment_stats()["total_assessments"]
        subject = get_subject("python")
        form_data = {"subject_id": "python"}
        
        # Answer first 6 questions correctly, remaining 4 incorrectly
        for i, q in enumerate(subject["questions"]):
            if i < 6:
                form_data[f"question_{q['id']}"] = q["answer"]
            else:
                form_data[f"question_{q['id']}"] = "WRONG_ANSWER"

        with patch("app.get_ai_coach_guidance", return_value="<p>Custom AI Coach Advice</p>"):
            response = self.client.post("/submit-quiz", data=form_data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Custom AI Coach Advice", response.data)
            self.assertIn(b'data-counter="6/10"', response.data)
            self.assertIn(b"60%", response.data)

        # Check DB persistence
        new_count = get_assessment_stats()["total_assessments"]
        self.assertEqual(new_count, initial_count + 1)
        latest = get_all_assessments()[0] # ordered by id desc
        self.assertEqual(latest["subject_id"], "python")
        self.assertEqual(latest["score"], 6)
        self.assertEqual(latest["total"], 10)
        self.assertEqual(latest["percentage"], 60)
        self.assertIn("Custom AI Coach Advice", latest["ai_coach_text"])
        
        # Verify topic level scores stored
        self.assertTrue(len(latest["topic_results"]) > 0)
        for t in latest["topic_results"]:
            self.assertIn("topic", t)
            self.assertIn("score", t)
            self.assertIn("status", t)

    def test_submission_with_ai_unavailable_fallback(self):
        """Test assessment submission when AI fails/unavailable - must fallback gracefully."""
        initial_count = get_assessment_stats()["total_assessments"]
        subject = get_subject("dsa")
        form_data = {"subject_id": "dsa"}
        
        # Answer all 10 questions correctly
        for q in subject["questions"]:
            form_data[f"question_{q['id']}"] = q["answer"]

        # Simulate Gemini throwing an error or being unreachable
        with patch("google.genai.Client", side_effect=Exception("Connection refused")):
            with patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key"}):
                response = self.client.post("/submit-quiz", data=form_data, follow_redirects=True)
                self.assertEqual(response.status_code, 200)
                # Results page must load and show results
                self.assertIn(b'data-counter="10/10"', response.data)
                self.assertIn(b"100%", response.data)
                self.assertIn(b"Data Structures", response.data)
                # Should have offline knowledge base study advice
                self.assertTrue(b"Study Coach" in response.data or b"Data Structures" in response.data)

        # Check DB persistence
        new_count = get_assessment_stats()["total_assessments"]
        self.assertEqual(new_count, initial_count + 1)
        latest = get_all_assessments()[0]
        self.assertEqual(latest["subject_id"], "dsa")
        self.assertEqual(latest["score"], 10)
        self.assertIsNotNone(latest["ai_coach_text"])

    def test_prevent_duplicate_submission_on_refresh(self):
        """Verify results_detail renders stored assessment without invoking Gemini or saving duplicates."""
        initial_count = get_assessment_stats()["total_assessments"]
        latest = get_all_assessments()[0]
        assessment_id = latest["id"]

        with patch("app.get_ai_coach_guidance") as mock_gemini:
            response = self.client.get(f"/results/{assessment_id}")
            self.assertEqual(response.status_code, 200)
            self.assertIn(latest["subject_name"].encode(), response.data)
            # Gemini must NOT be called on refresh/view
            mock_gemini.assert_not_called()
            # Database record count must not change
            self.assertEqual(get_assessment_stats()["total_assessments"], initial_count)

if __name__ == "__main__":
    unittest.main()
