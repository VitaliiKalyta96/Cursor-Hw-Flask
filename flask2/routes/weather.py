from flask import request, render_template, jsonify
from app import app
from config import Config
import requests


data_weather = {}

@app.route('/weather')
def weather():
    city = request.args.get('city')
    response = requests.get(
        Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
    )  

    return response.json()

@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')
    
@app.route('/weather2_cities')
def weather2_cities():
    cities = request.args.get('cities')
    for city in cities.split(' '):
        response = requests.get(
            Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
        )
        data_weather[city] = response.json()
    return jsonify(data_weather)
