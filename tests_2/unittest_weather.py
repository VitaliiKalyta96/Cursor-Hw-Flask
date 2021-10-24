import flask_unittest
from app import app
from .conftest import client


class TestFoo(flast_unittest.ClientTestCase):

    def test_weather(self, client):
        response = client.get('/weather?city=Kiev')
        self.assertJsonEqual(response.json['location']['name'], "Kiev")
        self.assertStatus(response.response_code, 200)
