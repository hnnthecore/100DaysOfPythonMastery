"""
Day 63 – Passing Data from Python to HTML using Flask

Today we learn:
- How Flask sends data to templates
- What Jinja placeholders {{ }} mean
- How HTML becomes dynamic
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    This route sends data from Python to HTML.

    render_template():
    - first argument = HTML file name
    - keyword arguments = data sent to HTML
    """
    return render_template(
        "index.html",
        username="Rick",
        role="Python Developer",
        skills=["Flask", "Python", "Web Development"]
    )


@app.route("/profile")
def profile():
    """
    Demonstrates multiple data types being passed to HTML:
    - strings
    - numbers
    - lists
    """
    user_data = {
        "name": "Rick",
        "experience": 2,
        "projects": 60
    }

    return render_template("profile.html", user=user_data)


if __name__ == "__main__":
    app.run(debug=True)
