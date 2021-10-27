import unittest

from app import app
from flask import Flask
from flask import render_template
from flask_testing import TestCase


class TestW(unittest.TestCase):

    def test_weather_1(self, client):
        response = self.client.get('/weather?city=Ternopil')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['location']['name'], "Ternopil")
        
        
def create_app(cfg=None):
    app = Flask(__name__)
    # app.config['DEBUG'] = True
    # app.config['SERVER_NAME'] = 'localhost'
    return app
    
class TestWw(unittest.TestCase):

    def setUp(self):
        self.app = create_app('mytest')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        self.client = self.app.test_client()

    @self.app.route("/get-your-weather")
    def yourWeather():
        return render_template('weather.html')

    def test_weather_true(self):
        response = self.client.get('/get-your-weather')
        self.assertTrue('City' in response.get_data(as_text=True))

    def test_weather_false(self):
        response = self.client.get('/get-your-weather')
        self.assertFalse('Notcity' in response.get_data(as_text=True))
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
unittest.TextTestRunner(verbosity=2).run(suite)        

class TestRender(TestCase):
        
    def test_save(self):
        response = self.client.get("/save")
        self.assertRedirects(response, "/display-text")
        
    def test_index():
        try:
            self.client.get("/")
            self.assert_template_used(Config.WEATHER_API_KEY)
        except RuntimeError:
            pass
                       
    def test_text(self):
        try:
            self.client.get("/display-text")
            self.assert_context("text", "text_global")
        except RuntimeError:
            pass
