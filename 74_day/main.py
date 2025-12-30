"""
Day 74 – REST API with Flask & SQLite

Adds a JSON API layer on top of the Notes App.
"""

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    jsonify,
    request,
    abort,
)
from forms import NoteForm
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "day74-notes-api"

DB_NAME = "notes.db"


# ---------- DATABASE HELPERS ----------

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


# ---------- HTML ROUTES (UNCHANGED) ----------

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

    if not note:
        abort(404)

    form = NoteForm(title=note["title"], content=note["content"])

    if form.validate_on_submit():
        conn.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (form.title.data, form.content.data, note_id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("view_notes"))

    conn.close()
    return render_template("edit_note.html", form=form)


@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("view_notes"))


# ---------- API ROUTES (NEW) ----------

@app.route("/api/notes", methods=["GET"])
def api_get_notes():
    conn = get_db_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()

    return jsonify([
        {"id": n["id"], "title": n["title"], "content": n["content"]}
        for n in notes
    ])


@app.route("/api/notes/<int:note_id>", methods=["GET"])
def api_get_note(note_id):
    conn = get_db_connection()
    note = conn.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()
    conn.close()

    if not note:
        return jsonify({"error": "Note not found"}), 404

    return jsonify({
        "id": note["id"],
        "title": note["title"],
        "content": note["content"]
    })


@app.route("/api/notes", methods=["POST"])
def api_create_note():
    data = request.get_json()

    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (data["title"], data["content"])
    )
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "message": "Note created",
        "id": note_id
    }), 201


@app.route("/api/notes/<int:note_id>", methods=["PUT"])
def api_update_note(note_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    conn = get_db_connection()
    result = conn.execute(
        "UPDATE notes SET title = ?, content = ? WHERE id = ?",
        (data.get("title"), data.get("content"), note_id)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({"error": "Note not found"}), 404

    return jsonify({"message": "Note updated"})


@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def api_delete_note(note_id):
    conn = get_db_connection()
    result = conn.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({"error": "Note not found"}), 404

    return jsonify({"message": "Note deleted"})


# ---------- RUN ----------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
