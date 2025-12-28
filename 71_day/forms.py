"""
WTForms definitions for Coffee & Wifi app.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

RATING_CHOICES = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐")
]


class CafeForm(FlaskForm):
    name = StringField(
        "Cafe Name",
        validators=[
            DataRequired(),
            Length(min=3, message="Name must be at least 3 characters.")
        ]
    )

    location = StringField(
        "Location",
        validators=[DataRequired()]
    )

    wifi = SelectField(
        "WiFi Strength",
        choices=RATING_CHOICES,
        validators=[DataRequired()]
    )

    coffee = SelectField(
        "Coffee Quality",
        choices=RATING_CHOICES,
        validators=[DataRequired()]
    )

    submit = SubmitField("Add Cafe")
