from datetime import datetime
from flask import render_template
from flask.ext.login import login_required
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', current_time=datetime.utcnow())
    
# login_required decorator provided by Flask-Login
@main.route('/secret') 
@login_required
def secret():
    return 'Only authenticated users are allowed!'
