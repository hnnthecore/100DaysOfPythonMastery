"""
Day 77 – URL Shortener with Analytics

Key idea:
- Track behavior, not just data
- Every redirect becomes an analytics event
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string
from datetime import datetime

app = Flask(__name__)
DB_NAME = "analytics.db"


# ---------------- DATABASE HELPERS ----------------

def get_db():
    # Create SQLite connection with dict-style rows
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Two tables:
    1. urls       → stores short ↔ long mapping
    2. clicks     → stores analytics per click
    """
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE,
            original_url TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url_id INTEGER,
            ip_address TEXT,
            clicked_at TEXT,
            FOREIGN KEY (url_id) REFERENCES urls(id)
        )
    """)

    conn.commit()
    conn.close()


# ---------------- UTILS ----------------

def generate_code(length=6):
    """
    Generates a random short code.
    """
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original_url = request.form["url"]
        short_code = generate_code()

        conn = get_db()

        # Save the URL mapping
        cursor = conn.execute(
            "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
            (short_code, original_url)
        )

        conn.commit()
        conn.close()

        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):
    """
    This route does TWO things:
    1. Redirects user
    2. Logs analytics
    """
    conn = get_db()

    url = conn.execute(
        "SELECT * FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()

    if not url:
        conn.close()
        return redirect("/")

    # ---- ANALYTICS LOGGING (CRITICAL PART) ----
    conn.execute(
        "INSERT INTO clicks (url_id, ip_address, clicked_at) VALUES (?, ?, ?)",
        (
            url["id"],
            request.remote_addr,
            datetime.utcnow().isoformat()
        )
    )

    conn.commit()
    conn.close()

    return redirect(url["original_url"])


@app.route("/analytics/<short_code>")
def analytics(short_code):
    """
    Shows analytics for a specific short URL.
    """
    conn = get_db()

    url = conn.execute(
        "SELECT * FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()

    if not url:
        conn.close()
        return redirect("/")

    clicks = conn.execute(
        "SELECT * FROM clicks WHERE url_id = ? ORDER BY clicked_at DESC",
        (url["id"],)
    ).fetchall()

    total_clicks = len(clicks)

    conn.close()

    return render_template(
        "analytics.html",
        short_code=short_code,
        original_url=url["original_url"],
        total_clicks=total_clicks,
        clicks=clicks
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
