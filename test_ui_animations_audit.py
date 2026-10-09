import unittest
import re
import requests

BASE_URL = "http://127.0.0.1:5001"

class TestUIAnimationAudit(unittest.TestCase):
    def test_01_static_assets_available(self):
        # Check style.css
        res_css = requests.get(f"{BASE_URL}/static/style.css")
        self.assertEqual(res_css.status_code, 200)
        css_text = res_css.text
        
        # Verify keyframes
        self.assertIn("@keyframes heroFadeUp", css_text)
        self.assertIn("@keyframes ambientGlow", css_text)
        self.assertIn("@keyframes popIn", css_text)
        self.assertIn("@keyframes growBarX", css_text)
        self.assertIn("@keyframes quizCardIn", css_text)
        self.assertIn("@media (prefers-reduced-motion: reduce)", css_text)
        
        # Verify card & button styles
        self.assertIn(".subject-card:hover", css_text)
        self.assertIn(".subject-icon-box", css_text)
        self.assertIn(".quiz-option-label.selected-option", css_text)
        self.assertIn(".bar-chart-fill", css_text)
        self.assertIn(".reveal-on-scroll", css_text)
        self.assertIn(".reveal-on-scroll.is-revealed", css_text)
        
        # Check animations.js
        res_js = requests.get(f"{BASE_URL}/static/animations.js")
        self.assertEqual(res_js.status_code, 200)
        js_text = res_js.text
        self.assertIn("initScrollReveal", js_text)
        self.assertIn("animateCounterElement", js_text)
        self.assertIn("IntersectionObserver", js_text)
        self.assertIn("prefers-reduced-motion", js_text)

    def test_02_dashboard_page(self):
        res = requests.get(f"{BASE_URL}/")
        self.assertEqual(res.status_code, 200)
        html = res.text
        self.assertIn('animations.js', html)
        self.assertIn('data-counter', html)
        self.assertIn('reveal-on-scroll', html)
        self.assertIn('hero-fade', html)

    def test_03_subjects_page(self):
        res = requests.get(f"{BASE_URL}/subjects")
        self.assertEqual(res.status_code, 200)
        html = res.text
        self.assertIn('animations.js', html)
        self.assertIn('reveal-on-scroll', html)
        self.assertIn('subject-progress-fill', html)
        # Verify all 6 subjects are present
        self.assertIn('Python Programming', html)
        self.assertIn('Machine Learning', html)
        self.assertIn('Data Structures', html)
        self.assertIn('Computer Networks', html)
        self.assertIn('Database Management Systems', html)
        self.assertIn('Operating Systems', html)

    def test_04_quiz_page(self):
        res = requests.get(f"{BASE_URL}/quiz/python")
        self.assertEqual(res.status_code, 200)
        html = res.text
        self.assertIn('animations.js', html)
        self.assertIn('quiz-progress-bar', html)
        self.assertIn('quiz-card', html)
        self.assertIn('quiz-option-label', html)
        self.assertIn('handleOptionSelect', html)
        self.assertIn('updateUI', html)

    def test_05_progress_page(self):
        res = requests.get(f"{BASE_URL}/progress")
        self.assertEqual(res.status_code, 200)
        html = res.text
        self.assertIn('animations.js', html)
        self.assertIn('data-counter', html)
        self.assertIn('reveal-on-scroll', html)
        self.assertIn('filterHistory', html)

    def test_06_resources_page(self):
        res = requests.get(f"{BASE_URL}/resources")
        self.assertEqual(res.status_code, 200)
        html = res.text
        self.assertIn('animations.js', html)
        self.assertIn('reveal-on-scroll', html)
        self.assertIn('resource-card', html)

    def test_07_results_page(self):
        # Check if there is an existing result ID, e.g. 1
        res = requests.get(f"{BASE_URL}/results/1")
        if res.status_code == 200:
            html = res.text
            self.assertIn('animations.js', html)
            self.assertIn('data-counter', html)
            self.assertIn('reveal-on-scroll', html)
            self.assertIn('results-score-card', html)

if __name__ == '__main__':
    unittest.main()
