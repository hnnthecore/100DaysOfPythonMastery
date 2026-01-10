"""
Day 78 – System Status Monitor Dashboard

This app tracks the health status of services
and logs every status change.
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "monitor.db"


# ---------------- DATABASE HELPERS ----------------

def get_db():
    # Create SQLite connection with dict-style access
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Two tables:
    1. services → current status
    2. logs     → historical status changes
    """
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            status TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_id INTEGER,
            status TEXT,
            timestamp TEXT,
            FOREIGN KEY (service_id) REFERENCES services(id)
        )
    """)

    conn.commit()
    conn.close()


# ---------------- ROUTES ----------------

@app.route("/")
def dashboard():
    """
    Shows current status of all services.
    """
    conn = get_db()
    services = conn.execute("SELECT * FROM services").fetchall()
    conn.close()

    return render_template("dashboard.html", services=services)


@app.route("/add", methods=["GET", "POST"])
def add_service():
    """
    Add a new monitored service.
    """
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]

        conn = get_db()

        # Insert service
        cursor = conn.execute(
            "INSERT INTO services (name, status) VALUES (?, ?)",
            (name, status)
        )

        service_id = cursor.lastrowid

        # Log initial status
        conn.execute(
            "INSERT INTO logs (service_id, status, timestamp) VALUES (?, ?, ?)",
            (service_id, status, datetime.utcnow().isoformat())
        )

        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("add_service.html")


@app.route("/update/<int:service_id>/<status>")
def update_status(service_id, status):
    """
    Update service status and log the change.
    """
    conn = get_db()

    # Update current status
    conn.execute(
        "UPDATE services SET status = ? WHERE id = ?",
        (status, service_id)
    )

    # Log status change
    conn.execute(
        "INSERT INTO logs (service_id, status, timestamp) VALUES (?, ?, ?)",
        (service_id, status, datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


@app.route("/logs/<int:service_id>")
def view_logs(service_id):
    """
    View status history for a service.
    """
    conn = get_db()

    service = conn.execute(
        "SELECT * FROM services WHERE id = ?",
        (service_id,)
    ).fetchone()

    logs = conn.execute(
        "SELECT * FROM logs WHERE service_id = ? ORDER BY timestamp DESC",
        (service_id,)
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        services=[],
        logs=logs,
        service=service
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
