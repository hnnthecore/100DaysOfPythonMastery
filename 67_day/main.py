"""
Day 67 – Form Validation & Error Handling in Flask

Today we learn:
- How to validate user input manually
- How to handle empty / invalid submissions
- How to send error messages to templates
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handles both page load and form submission.
    Performs backend validation before accepting input.
    """

    username = None
    error = None

    if request.method == "POST":
        # Get user input safely
        username = request.form.get("username", "").strip()

        # VALIDATION STEP
        if not username:
            error = "Name cannot be empty."
        elif len(username) < 3:
            error = "Name must be at least 3 characters long."

    return render_template(
        "form.html",
        username=username,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
