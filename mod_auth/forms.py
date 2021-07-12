from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, InputRequired, Email


class RegisterForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    email = StringField('email', validators.Email)