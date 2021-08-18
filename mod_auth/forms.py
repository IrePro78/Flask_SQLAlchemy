from wtforms import Form, StringField, PasswordField, validators



class RegisterForm(Form):
    username = StringField('Username :', [validators.Length(min=5)])
    password = PasswordField('Password :', [validators.Length(min=6)])
    email = StringField('email', [validators.Email()])



class LoginForm(Form):
    username = StringField('Username :', [validators.Length(min=5)])
    password = PasswordField('Password :', [validators.Length(min=6)])
