"""
Day 82 – Choose Your Own Adventure Engine

Core idea:
The story is a graph.
Each scene (node) leads to other scenes via choices.
"""

from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "story.db"


# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Two tables:
    1. scenes   → story content
    2. choices  → links between scenes
    """
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS scenes (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            is_ending INTEGER DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS choices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scene_id INTEGER,
            choice_text TEXT,
            next_scene INTEGER,
            FOREIGN KEY (scene_id) REFERENCES scenes(id)
        )
    """)

    # Seed story only once
    conn.execute("""
        INSERT OR IGNORE INTO scenes (id, text, is_ending)
        VALUES
        (1, 'You wake up in a dark forest. Two paths lie ahead.', 0),
        (2, 'You follow the left path and find a hidden village.', 0),
        (3, 'You take the right path and fall into a trap. Game Over.', 1),
        (4, 'The villagers welcome you. You are safe. The End.', 1)
    """)

    conn.execute("""
        INSERT OR IGNORE INTO choices (scene_id, choice_text, next_scene)
        VALUES
        (1, 'Take the left path', 2),
        (1, 'Take the right path', 3),
        (2, 'Enter the village', 4)
    """)

    conn.commit()
    conn.close()


# ---------------- ROUTES ----------------

@app.route("/")
def start():
    # Always start at scene 1
    return redirect(url_for("scene", scene_id=1))


@app.route("/scene/<int:scene_id>")
def scene(scene_id):
    """
    Loads a scene and its available choices.
    """
    conn = get_db()

    scene = conn.execute(
        "SELECT * FROM scenes WHERE id = ?",
        (scene_id,)
    ).fetchone()

    choices = conn.execute(
        "SELECT * FROM choices WHERE scene_id = ?",
        (scene_id,)
    ).fetchall()

    conn.close()

    return render_template(
        "story.html",
        scene=scene,
        choices=choices
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
