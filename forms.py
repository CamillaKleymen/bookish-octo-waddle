from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, PasswordField, SubmitField)

from wtforms.validators import DataRequired

# form for registration
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Enter a name")])
    email = EmailField("email", validators=[DataRequired("Enter an email")])
    password = PasswordField("password", validators=[DataRequired("Enter a password")])
    password2 = PasswordField("password2", validators=[DataRequired("Repeat a password")])

    button = SubmitField("Registrate")

class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired("Enter an email")])
    password = PasswordField("password", validators=[DataRequired("Enter a password")])

    button = SubmitField("Sign in ")
