from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField(
        "Note Title",
        validators=[
            DataRequired(message="Title is required."),
            Length(min=3, message="Title must be at least 3 characters.")
        ]
    )

    content = TextAreaField(
        "Note Content",
        validators=[
            DataRequired(message="Content cannot be empty."),
            Length(min=10, message="Content must be at least 10 characters.")
        ]
    )

    submit = SubmitField("Save Note")
