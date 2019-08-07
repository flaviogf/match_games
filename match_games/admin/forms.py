from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class AuthenticateForm(FlaskForm):
    email = StringField('Email',
                        validators=[Email(), DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Sign In')
