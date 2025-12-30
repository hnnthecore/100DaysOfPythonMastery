from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField(
        "Note Title",
        validators=[
            DataRequired(),
            Length(min=3)
        ]
    )

    content = TextAreaField(
        "Note Content",
        validators=[
            DataRequired(),
            Length(min=10)
        ]
    )

    submit = SubmitField("Save")
