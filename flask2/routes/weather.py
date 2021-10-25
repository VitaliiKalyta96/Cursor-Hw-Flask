from flask import request, render_template
from app import app
from config import Config
import requests


@app.route('/weather')
def weather():
    city = request.args.get('city')
    city_2 = request.args.get('city2')
    response = requests.get(
        Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
    )
    

    return response.json()


@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')
