"""
Day 71 – Coffee & Wifi Rating App (Mini Project)

A complete mini Flask application that:
- Collects cafe details
- Validates input using WTForms
- Displays submitted cafes
"""

from flask import Flask, render_template, redirect, url_for
from forms import CafeForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "day71-coffee-wifi"

# Temporary in-memory storage (will be replaced by DB later)
cafes = []


@app.route("/", methods=["GET", "POST"])
def add_cafe():
    """
    Add a new cafe using WTForms.
    """
    form = CafeForm()

    if form.validate_on_submit():
        cafe = {
            "name": form.name.data,
            "location": form.location.data,
            "wifi": form.wifi.data,
            "coffee": form.coffee.data
        }

        cafes.append(cafe)

        return redirect(url_for("list_cafes"))

    return render_template("add_cafe.html", form=form)


@app.route("/cafes")
def list_cafes():
    """
    Display all submitted cafes.
    """
    return render_template("cafes.html", cafes=cafes)


if __name__ == "__main__":
    app.run(debug=True)
