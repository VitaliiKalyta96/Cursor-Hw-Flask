import unittest
from app import app


class TestAll(unittest.TestCase):

    def test_weather_2(self, client):
        response = self.client.get('/weather?city=Ternopil')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['location']['name'], "Ternopil")
        
