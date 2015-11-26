from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, PasswordField
from wtforms.validators import Required, Length


class BetaRegistration(Form):
    email = TextField('Email Address', validators=[Required(), Length(5, 256)])
    register = SubmitField('Register')

class SignIn(Form):
    username = TextField('Username', validators=[Required(), Length(5, 256)])
    password = PasswordField('Password', validators=[Required()])
    sign_in = SubmitField('Sign In')

