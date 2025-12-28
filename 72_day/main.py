"""
Day 72 – Notes App with SQLite

Today we learn:
- How SQLite works with Flask
- How to create tables
- How to insert and fetch records
"""

from flask import Flask, render_template, redirect, url_for
from forms import NoteForm
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "day72-notes-app"

DB_NAME = "notes.db"


def get_db_connection():
    """
    Creates a database connection.
    row_factory allows dict-like access.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates the notes table if it does not exist.
    Runs once when app starts.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def add_note():
    """
    Add a new note to the database.
    """
    form = NoteForm()

    if form.validate_on_submit():
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (form.title.data, form.content.data)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_notes"))

    return render_template("add_note.html", form=form)


@app.route("/notes")
def view_notes():
    """
    Fetch and display all saved notes.
    """
    conn = get_db_connection()
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()

    return render_template("notes.html", notes=notes)


if __name__ == "__main__":
    init_db()   # Ensure DB exists
    app.run(debug=True)
