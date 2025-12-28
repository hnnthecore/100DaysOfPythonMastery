"""
WTForms definitions live here.
This keeps validation logic OUT of routes.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class NameForm(FlaskForm):
    """
    A simple WTForms form with validation rules.
    """

    name = StringField(
        "Your Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(min=3, message="Name must be at least 3 characters."),
            Regexp("^[A-Za-z]+$", message="Only letters allowed.")
        ]
    )

    submit = SubmitField("Submit")
