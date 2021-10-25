import unittest
from app import app


class TestAll(unittest.TestCase):

    def test_weather(self, client):
        response = self.client.get('/weather?city=Ternopil')
        self.assertEqual(200, response.status_code)
        self.assertIn(response.json['location']['name'], "Ternopil")
        
if __name__ == '__main__':
    unittest.main()
