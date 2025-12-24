"""
Day 68 – Contact Form System in Flask

Today we build a real multi-field form:
- Name
- Email
- Message

We validate input properly and show
clear feedback to the user.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def contact():
    """
    Handles contact form display and submission.
    """

    errors = {}
    success = False

    # Default values to preserve input after submission
    form_data = {
        "name": "",
        "email": "",
        "message": ""
    }

    if request.method == "POST":
        # Get and clean input
        form_data["name"] = request.form.get("name", "").strip()
        form_data["email"] = request.form.get("email", "").strip()
        form_data["message"] = request.form.get("message", "").strip()

        # --- VALIDATION LOGIC ---

        if not form_data["name"]:
            errors["name"] = "Name is required."
        elif not form_data["name"].isalpha():
            errors["name"] = "Name must contain only letters."

        if not form_data["email"]:
            errors["email"] = "Email is required."
        elif "@" not in form_data["email"] or "." not in form_data["email"]:
            errors["email"] = "Enter a valid email address."

        if not form_data["message"]:
            errors["message"] = "Message cannot be empty."
        elif len(form_data["message"]) < 10:
            errors["message"] = "Message must be at least 10 characters long."

        # If no validation errors → success
        if not errors:
            success = True
            # In real apps, data would be:
            # - saved to database
            # - emailed
            # - logged
            form_data = {"name": "", "email": "", "message": ""}

    return render_template(
        "contact.html",
        errors=errors,
        success=success,
        form_data=form_data
    )


if __name__ == "__main__":
    app.run(debug=True)
