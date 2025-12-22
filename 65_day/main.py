"""
Day 65 – Static Files in Flask

Today we learn:
- How Flask serves static files (CSS)
- Why static files are separated from templates
- How to link CSS using url_for()
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the home page.
    Styling is handled by CSS from the static folder.
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Another page using the same CSS file.
    """
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
