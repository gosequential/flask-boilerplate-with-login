from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin, AnonymousUserMixin
import datetime
#from . import db, login_manager
from . import db

# Beta Requests for Datapir
class BetaRequest(db.Model):
    __tablename__="BetaRequests"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))

    def __repr__(self):
        return 'Beta Subscriber: %r' % self.email


# Flask-Login requires a callback function that loads a user, given the identifier
#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))

# Beta Requests for Datapir
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256))
    password = db.Column(db.String(256))

    def __repr__(self):
        return 'User: %r' % self.username

# Database for the current_weather api
class CurrentWeather(db.Model):
    __tablename__="current_weather"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(32))
    country = db.Column(db.String(32))
    conditions = db.Column(db.String(32))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    windspeed = db.Column(db.Float)
    wind_direction = db.Column(db.Integer)
    sunrise = db.Column(db.Integer)
    sunset = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    utc_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return 'Current Weather - %s' % self.city


