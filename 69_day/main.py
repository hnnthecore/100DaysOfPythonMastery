"""
Day 69 – Introduction to Flask-WTForms

Today we learn:
- What WTForms is
- Why it exists
- How Flask integrates with it
"""

from flask import Flask, render_template
from forms import NameForm

app = Flask(__name__)

# WTForms needs a secret key for CSRF protection
app.config["SECRET_KEY"] = "day69-wtforms-key"


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handles form rendering and validation using WTForms.
    """
    form = NameForm()

    if form.validate_on_submit():
        # If validation passes, form data is accessible safely
        username = form.name.data
        return render_template("form.html", form=form, username=username)

    return render_template("form.html", form=form, username=None)


if __name__ == "__main__":
    app.run(debug=True)
