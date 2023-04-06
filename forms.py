from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, Form, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class Phrase(Form):
    phrase = TextAreaField("", validators=[DataRequired(message='Input first_name')])