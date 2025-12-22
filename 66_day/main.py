"""
Day 66 – Handling User Input in Flask (GET & POST)

Today we learn:
- How HTML forms send data to Flask
- Difference between GET and POST
- How Flask receives user input
- How Bootstrap improves UI without changing logic
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    This route handles BOTH:
    - GET  → when page is first loaded
    - POST → when form is submitted
    """

    username = None

    # request.method tells us HOW the page was accessed
    if request.method == "POST":
        # request.form contains data sent using POST
        # 'username' comes from the input's name attribute
        username = request.form.get("username")

    return render_template("form.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
