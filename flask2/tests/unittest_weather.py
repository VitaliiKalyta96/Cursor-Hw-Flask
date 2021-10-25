import unittest

# import flask_unittest
from app import app
# from .conftest import client


# class TestWeather(flast_unittest.ClientTestCase):
#
#     def test_weather(self, client):
#         response = client.get('/weather?city=Kiev')
#         self.assertJsonEqual(response.json['location']['name'], "Kiev")
#         self.assertStatus(response.response_code, 200)
        

class TestAll(unittest.TestCase):

    def test_weather(self, client):
        response = client.get('/weather?city=Kiev')
        self.assertIn(response.json['location']['name'], "Kiev")
        self.assertEqual(response.response_code, 200)
    
#     with app.test_request_context('/save', method='POST'):
#         assert request.path == '/save'
#         assert request.method == 'POST'
#
#     def test_text_new(self):
#         response = self.app.get('/', follow_render_template=True)
#         self.assertEqual(response.status_code, 200)
#
#
# if __name__ == "__main__":
#     flask_unittest.main()
#     unittest.main()
