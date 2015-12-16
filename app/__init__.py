from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_restful import Api
from config import config

mail = Mail()
db = SQLAlchemy()

#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('../instance/config.py')
    config[config_name].init_app(app)
    
    mail.init_app(app)
    db.init_app(app)

    #login_manager.init_app(app)
    
    from main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    #from auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from api_1_0 import api as api_blueprint
    #from resources.eruditorium import Weather, PricingData
    #api = Api(api_blueprint)
    #api.add_resource(Weather, '/rumbleboard/v1/weather')
    #api.add_resource(PricingData, '/rumble/v1/pricing-data')
    app.register_blueprint(api_blueprint, url_prefix = '/api/v1.0')
    

    return app
