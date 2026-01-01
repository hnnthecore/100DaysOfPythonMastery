"""
Day 76 – URL Shortener (Flask + SQLite)

Goal:
Convert long URLs into short codes
and redirect users back to original URLs.
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

DB_NAME = "urls.db"


# ---------------- DATABASE SETUP ----------------

def get_db():
    # Create a connection to SQLite database
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # Create table to store short → long URL mappings
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------- HELPER FUNCTIONS ----------------

def generate_short_code(length=6):
    """
    Generates a random alphanumeric string.
    This will act as the short URL key.
    """
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original_url = request.form["url"]

        # Generate a short unique key
        short_code = generate_short_code()

        conn = get_db()

        # Store mapping in database
        conn.execute(
            "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
            (short_code, original_url)
        )

        conn.commit()
        conn.close()

        # Build full short URL for display
        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):
    """
    When someone visits the short URL,
    look up the original URL and redirect.
    """
    conn = get_db()

    # Fetch original URL using short code
    result = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()

    conn.close()

    # If short code exists, redirect to original URL
    if result:
        return redirect(result["original_url"])

    # Otherwise, go back to home
    return redirect("/")


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
