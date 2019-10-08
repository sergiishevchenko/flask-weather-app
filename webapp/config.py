import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
WEATHER_DEFAULT_CITY = 'Lausanne, Switzerland'
WEATHER_API_KEY = '94df97d243cc4535be7162743191409'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

SECRET_KEY = "sdfqwrefdsfdsafret439589049rjskjkgfj"

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
