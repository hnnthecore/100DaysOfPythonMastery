"""
Day 70 – WTForms Definitions

Advanced form fields with validators.
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    EmailField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
    """
    A realistic multi-field WTForm.
    """

    name = StringField(
        "Full Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(min=3, message="Name must be at least 3 characters.")
        ]
    )

    email = EmailField(
        "Email Address",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Enter a valid email address.")
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Message cannot be empty."),
            Length(min=10, message="Message must be at least 10 characters.")
        ]
    )

    submit = SubmitField("Register")
