from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required, Length


class BetaRegistration(Form):
    email = TextField('Email Address', validators=[Required(), Length(5, 256)])
    submit = SubmitField('Submit')