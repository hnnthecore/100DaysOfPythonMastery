"""
Day 64 – Template Inheritance in Flask

Today we learn:
- How Flask reuses HTML layouts
- Why base.html exists
- How child templates extend a parent template
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the home page.
    The HTML content comes from index.html,
    but the layout comes from base.html.
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Another page using the SAME base layout.
    Only the content block changes.
    """
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
