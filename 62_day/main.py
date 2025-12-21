"""
Day 62 – Rendering HTML with Flask

Today we learn:
- How Flask returns HTML instead of plain text
- What render_template() does
- Why Flask needs a 'templates' folder
"""

from flask import Flask, render_template

# -------------------------------------------------
# CREATE FLASK APP
# -------------------------------------------------
# __name__ tells Flask where this file is located
# so it can find the templates folder correctly.

app = Flask(__name__)


# -------------------------------------------------
# HOME ROUTE
# -------------------------------------------------
@app.route("/")
def home():
    """
    This route renders an HTML file instead of plain text.

    render_template():
    - finds the HTML file inside the 'templates' folder
    - reads the file
    - sends it as an HTTP response to the browser
    """
    return render_template("index.html")


# -------------------------------------------------
# ABOUT ROUTE
# -------------------------------------------------
@app.route("/about")
def about():
    """
    Multiple routes can render different HTML pages.
    Each page is still controlled by Python.
    """
    return render_template("about.html")


# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
