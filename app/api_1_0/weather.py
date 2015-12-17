from datetime import datetime
from pytz import timezone
from flask import render_template, redirect, abort, jsonify
from flask.ext.login import login_required
from . import api  # Get the Blueprint
from .. import db
from ..models import BetaRequest, User, CurrentWeather
from .decorators import crossdomain

class CityWeather(object):
    """ Create city weather objects of current conditions """

    # The class constructor - actually an initializer
    def __init__(self, city):
        current_weather = CurrentWeather.query.filter_by(city = city).order_by(CurrentWeather.id.desc()).first()
        self._apikey = "7b19f1486bfeddcc13608a1b8e621522"
        self._city = city
        self._country = current_weather.country
        self._conditions = current_weather.conditions
        self._temperature = current_weather.temperature
        self._humidity = current_weather.humidity
        self._windspeed = current_weather.windspeed
        self._wind_direction = current_weather.wind_direction
        self._sunrise = current_weather.sunrise
        self._sunset = current_weather.sunset
        self._latitude = current_weather.latitude
        self._longitude = current_weather.longitude
        self._local_time = None

    @property
    def weather_data(self):
        _weather_data = {
            "city": self._city,
            "country": self._country,
            "conditions": self._normalizeConditions(self._conditions), # call _normalizeConditions as a member function on the instance, self.
            "temperature_C": int(self._temperature - 273),
            "humidity": int(self._humidity),
            "windspeed_kph": ("%.2f" % self._windspeed),
            "wind_direction": self._ordinalDirection(self._wind_direction),
            "sunrise": self._time(self._sunrise),
            "sunset": self._time(self._sunset),
            "latitude": self._latitude,
            "longitude": self._longitude,
            "local_time": datetime.now(timezone('Europe/Prague')).strftime('%H:%M:%S'),
            "local_date": datetime.now(timezone('Europe/Prague')).strftime('%B %d, %Y'),
            "ampm": datetime.now(timezone('Europe/Prague')).strftime('%p')
        }
        return _weather_data

    def _normalizeConditions(self, description):
        return "wi wi-cloudy"

    def _ordinalDirection(self, direction):
        if direction < 30:
            return "North"
        elif direction < 60:
            return "Northeast"
        elif direction < 120:
            return "East"
        elif direction < 150:
            return "Southeast"
        elif direction < 210:
            return "South"
        elif direction < 240:
            return "Southwest"
        elif direction < 300:
            return "West"
        elif direction < 330:
            return "Northwest"
        else:
            return "North"

    def _time(self, epoch):
        tz = timezone('Europe/Prague')
        return datetime.fromtimestamp(epoch, tz).strftime('%H:%M:%S')


@api.route('/')
def api_root():
    return "Welcome to the Datapir (API) Signup / Signin"

@api.route('/<string:uid>')
def api_signin(uid):
    return "<p>Hello " + uid + ", your api key checks out.</p><p>Your resources are as follows...</p><p><a href='/api/enochroot/weather'>Weather</a></p>"

@api.route('/weather/<string:city>', methods=['GET'])
@crossdomain(origin='http://www.rumbleboard.com', headers="Authorization")
def get_weather_data(city):
    city = CityWeather('Prague')
    weather_data = city.weather_data
    return jsonify(weather_data)



"""
@main.route('/api/weather/<city>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers="Authorization")
def api_weather(city):
    today = date.today().strftime("%B %d, %Y")

    weather_data = getWeather('Prague')

    if city == 'prague':
        return jsonify( city="Prague",
                        country="Czech Republic",
                        conditions="cloudy",
                        date=today,
                        temp=int(weather_data['main']['temp']) - 273,
                        humidity=weather_data['main']['humidity'],
                        wind=weather_data['wind']['speed'])
    else:
        return jsonify( city="London",
                        country="United Kingdom",
                        conditions="Rain",
                        date="December 10, 2015",
                        temp="12",
                        humidity="64",
                        wind="5")

def getWeather(city):
    url ='http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=7b19f1486bfeddcc13608a1b8e621522' % (city)
    response = requests.get(url)
    return json.loads(response.text)

"""


