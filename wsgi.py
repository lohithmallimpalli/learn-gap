"""
LearnGap — WSGI Application Entry Point
Used by production WSGI servers such as Gunicorn or uWSGI:
    gunicorn --bind 0.0.0.0:$PORT wsgi:app
"""

from app import app

if __name__ == "__main__":
    app.run()
