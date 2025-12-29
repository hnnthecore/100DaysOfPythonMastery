"""
Day 73 – Full CRUD Notes App with SQLite

Adds:
- Edit notes
- Delete notes
- Update database records
"""

from flask import Flask, render_template, redirect, url_for
from forms import NoteForm
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "day73-full-crud"

DB_NAME = "notes.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
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
    form = NoteForm()

    if form.validate_on_submit():
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (form.title.data, form.content.data)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("view_notes"))

    return render_template("add_note.html", form=form)


@app.route("/notes")
def view_notes():
    conn = get_db_connection()
    notes = conn.execute(
        "SELECT * FROM notes ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("notes.html", notes=notes)


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    conn = get_db_connection()
    note = conn.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    form = NoteForm(
        title=note["title"],
        content=note["content"]
    )

    if form.validate_on_submit():
        conn.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (form.title.data, form.content.data, note_id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("view_notes"))

    conn.close()
    return render_template(
        "edit_note.html",
        form=form,
        note_id=note_id
    )


@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("view_notes"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
