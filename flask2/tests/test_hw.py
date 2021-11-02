import unittest
import json
from app import app
from flask import Flask


class TestWeather(unittest.TestCase):

    def setUp(self):
        self.app = create_app('mytest')
        self.client = self.app.test_client()

    def test_weather_1(self):
        response = self.client.get('/weather?city=Lviv')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['location']['name'], "Ternopil")
        
    def test_your_weather_2(self):
        response = self.client.get('/get-your-weather')
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        
    def test_weather2_cities_3(self):
        response = self.client.get('/weather2_cities?cities=Lviv%20Ternopil')
        self.assertEqual(response.status_code, 200)
