"""
Day 81 – Digital Time Capsule

Core idea:
Messages are locked until a future date.
Backend decides WHEN content is visible.
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "capsule.db"


# ---------------- DATABASE ----------------

def get_db():
    # Connect to SQLite with dictionary-style rows
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Stores messages and unlock dates.
    """
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS capsules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            unlock_date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def create_capsule():
    """
    Create a new time capsule.
    """
    if request.method == "POST":
        message = request.form["message"]
        unlock_date = request.form["unlock_date"]

        conn = get_db()
        conn.execute(
            "INSERT INTO capsules (message, unlock_date, created_at) VALUES (?, ?, ?)",
            (
                message,
                unlock_date,
                datetime.utcnow().isoformat()
            )
        )
        conn.commit()
        conn.close()

        return redirect(url_for("view_capsule"))

    return render_template("create.html")


@app.route("/view")
def view_capsule():
    """
    Show all capsules.
    Locked or unlocked depends on current date.
    """
    conn = get_db()
    capsules = conn.execute(
        "SELECT * FROM capsules ORDER BY created_at DESC"
    ).fetchall()
    conn.close()

    now = datetime.utcnow()

    return render_template(
        "view.html",
        capsules=capsules,
        now=now
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
