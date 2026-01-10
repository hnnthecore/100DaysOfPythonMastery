"""
Day 79 – Feature Flags & A/B Testing System

Core idea:
Backend decides which users see which features.
"""

from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "flags.db"


# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            rollout INTEGER
        )
    """)

    # Seed a feature if not exists
    conn.execute("""
        INSERT OR IGNORE INTO features (name, rollout)
        VALUES ('new_ui', 50)
    """)

    conn.commit()
    conn.close()


# ---------------- FEATURE LOGIC ----------------

def is_feature_enabled(feature_name, user_id):
    """
    Determines if a feature is enabled for a user.

    Uses hashing so:
    - Same user gets same experience
    - Rollout percentage is respected
    """
    conn = get_db()

    feature = conn.execute(
        "SELECT rollout FROM features WHERE name = ?",
        (feature_name,)
    ).fetchone()

    conn.close()

    if not feature:
        return False

    rollout = feature["rollout"]

    # Hash user_id to a stable number between 0–99
    hash_value = int(
        hashlib.sha256(user_id.encode()).hexdigest(),
        16
    ) % 100

    return hash_value < rollout


# ---------------- ROUTES ----------------

@app.route("/")
def dashboard():
    """
    Simulates a user visiting the app.
    """
    # Fake user ID (in real apps comes from auth)
    user_id = request.args.get("user", "guest")

    feature_on = is_feature_enabled("new_ui", user_id)

    return render_template(
        "dashboard.html",
        user_id=user_id,
        feature_on=feature_on
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
