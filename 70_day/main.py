"""
Day 70 – Advanced WTForms + Bootstrap

Today we learn:
- Using multiple WTForms fields
- Better validators
- Cleaner Bootstrap layout
"""

from flask import Flask, render_template
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "day70-advanced-wtforms"


@app.route("/", methods=["GET", "POST"])
def register():
    """
    Registration-style form using WTForms.
    """
    form = RegisterForm()
    success = False

    if form.validate_on_submit():
        # Access validated data safely
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # In real apps:
        # - save to DB
        # - send email
        # - trigger workflows
        success = True

        # Reset form after success
        form = RegisterForm()

    return render_template(
        "register.html",
        form=form,
        success=success
    )


if __name__ == "__main__":
    app.run(debug=True)
