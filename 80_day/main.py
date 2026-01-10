"""
Day 80 – Feature Flag Admin Panel

Admin users can control feature rollouts
without restarting or redeploying the app.
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "flags.db"


# ---------------- DATABASE ----------------

def get_db():
    # Connect to SQLite with dict-style rows
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    # Stores feature name and rollout percentage
    conn.execute("""
        CREATE TABLE IF NOT EXISTS features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            rollout INTEGER
        )
    """)

    # Seed feature if missing
    conn.execute("""
        INSERT OR IGNORE INTO features (name, rollout)
        VALUES ('new_ui', 50)
    """)

    conn.commit()
    conn.close()


# ---------------- FEATURE LOGIC ----------------

def is_feature_enabled(feature_name, user_id):
    """
    Determines feature availability for a user.
    Same user always gets same result.
    """
    conn = get_db()

    feature = conn.execute(
        "SELECT rollout FROM features WHERE name = ?",
        (feature_name,)
    ).fetchone()

    conn.close()

    if not feature:
        return False

    # Hash user_id → stable number between 0–99
    bucket = int(
        hashlib.sha256(user_id.encode()).hexdigest(),
        16
    ) % 100

    return bucket < feature["rollout"]


# ---------------- USER VIEW ----------------

@app.route("/")
def dashboard():
    # Simulated user identity
    user_id = request.args.get("user", "guest")

    feature_on = is_feature_enabled("new_ui", user_id)

    return render_template(
        "dashboard.html",
        user_id=user_id,
        feature_on=feature_on
    )


# ---------------- ADMIN VIEW ----------------

@app.route("/admin", methods=["GET", "POST"])
def admin():
    conn = get_db()

    if request.method == "POST":
        # Admin updates rollout percentage
        rollout = int(request.form["rollout"])

        conn.execute(
            "UPDATE features SET rollout = ? WHERE name = 'new_ui'",
            (rollout,)
        )
        conn.commit()

    feature = conn.execute(
        "SELECT * FROM features WHERE name = 'new_ui'"
    ).fetchone()

    conn.close()

    return render_template("admin.html", feature=feature)


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
