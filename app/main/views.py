from datetime import datetime
from flask import render_template, redirect
from flask.ext.login import login_required
from . import main
from .forms import BetaRegistration, SignIn
from .. import db
from ..models import BetaRequest, User

@main.route('/', methods=['GET', 'POST'])
def index():
    register = BetaRegistration()
    signin = SignIn()
    return render_template('main/index.html', form=register, signin=signin)

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


@main.route('/login', methods=['GET', 'POST'])
def login():
    user_login = SignIn()

    if user_login.validate_on_submit():
        entered_username = user_login.username.data
        entered_password = user_login.password.data
        try:
            user = User.query.filter_by(username = entered_username).first()
            if user.password == entered_password:
                return redirect('/construct')
        except:
            return redirect('/')
    return redirect('/')


@main.route('/construct', methods=['GET', 'POST'])
def console():

    return render_template('main/construct.html', message="Welcome to the Constructor...")





