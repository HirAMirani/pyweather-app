from flask import Flask, request, render_template
import requests
from datetime import date
from datetime import time
from datetime import datetime
import os


from requests import api

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def showWeather():
    API_KEY = os.environ['weather_forecast']
    city = request.form.get('city')
    WEB_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        str(city)+'&appid=' + API_KEY
    API_link = requests.get(WEB_link).json()
    location = API_link['name']
    condition = API_link['weather'][0]['main']
    description = API_link['weather'][0]['description']
    # url = "http://openweathermap.org/img/wn/10d@2x.png"
    # icon = requests.get(url)
    temp = str(round(float(API_link['main']['temp'] - 273.15)))
    dt = date.today()

    return render_template('index.html', description=description, dt=dt, location=location, temp=temp)


app.run()
