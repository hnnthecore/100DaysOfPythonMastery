"""
Day 83 – IFTTT-Style Rule Engine

Core idea:
IF <condition> THEN <action>
Backend evaluates rules dynamically.
"""

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_NAME = "rules.db"


# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Rules table stores simple IF → THEN logic.
    """
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            condition_key TEXT,
            condition_value TEXT,
            action TEXT
        )
    """)

    conn.commit()
    conn.close()


# ---------------- RULE EVALUATION ----------------

def evaluate_rules(input_data):
    """
    Checks all rules and returns matching actions.
    """
    conn = get_db()
    rules = conn.execute("SELECT * FROM rules").fetchall()
    conn.close()

    triggered_actions = []

    for rule in rules:
        # IF input matches rule condition → trigger action
        if input_data.get(rule["condition_key"]) == rule["condition_value"]:
            triggered_actions.append(rule["action"])

    return triggered_actions


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def create_rule():
    """
    Allows users to define new rules.
    """
    if request.method == "POST":
        key = request.form["condition_key"]
        value = request.form["condition_value"]
        action = request.form["action"]

        conn = get_db()
        conn.execute(
            "INSERT INTO rules (condition_key, condition_value, action) VALUES (?, ?, ?)",
            (key, value, action)
        )
        conn.commit()
        conn.close()

    return render_template("create_rule.html")


@app.route("/test", methods=["GET", "POST"])
def test_rules():
    """
    Tests rules against input.
    """
    actions = []

    if request.method == "POST":
        input_data = {
            "mood": request.form.get("mood"),
            "weather": request.form.get("weather"),
            "energy": request.form.get("energy")
        }

        actions = evaluate_rules(input_data)

    return render_template("test_rules.html", actions=actions)


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
