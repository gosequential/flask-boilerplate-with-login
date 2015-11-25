from datetime import datetime
from flask import render_template, redirect
from flask.ext.login import login_required
from . import main
from .forms import BetaRegistration
from .. import db
from ..models import BetaRequest

@main.route('/', methods=['GET', 'POST'])
def index():
    form = BetaRegistration()
    return render_template('main/index.html', form=form)

@main.route('/beta_registration', methods=['GET', 'POST'])
def beta_registration():
    beta_user_registration = BetaRegistration()

    if beta_user_registration.validate_on_submit():
        email = beta_user_registration.email.data
        new_beta_tester = BetaRequest(email=email)
        db.session.add(new_beta_tester)
        db.session.commit()

    return render_template('main/beta_registration.html')


# login_required decorator provided by Flask-Login
@main.route('/secret') 
@login_required
def secret():
    return 'Only authenticated users are allowed!'
