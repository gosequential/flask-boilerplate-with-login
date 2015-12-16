#!/usr/bin/env python

import MySQLdb, requests, json
from datetime import datetime

# Grab data from OpenWeatherMap
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=7b19f1486bfeddcc13608a1b8e621522' % ('prague')
response = requests.get(url)
data = json.loads(response.text)

# Assign data to variables for easy database storage
city = "Prague"
country = "Czech Republic"
conditions = data['weather'][0]['main']
temperature = data['main']['temp']
humidity = data['main']['humidity']
windspeed = data['wind']['speed']
wind_direction = data['wind']['deg']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
utc_datetime = datetime.utcnow()
print datetime.utcnow()
# Setup and commit to db


db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="dakar5",
                     db="datapir",
                     port=int(3306))

# Create a Cursor object to execute queries upon
cur = db.cursor()

# Prep the SQL
sql = """INSERT INTO current_weather (city, country, conditions, temperature, humidity, windspeed, wind_direction, 
            sunrise, sunset, latitude, longitude, utc_datetime) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
args = (city, country, conditions, temperature, humidity, windspeed, wind_direction, sunrise, sunset, latitude, longitude, utc_datetime)

cur.execute(sql, args)
db.commit()




