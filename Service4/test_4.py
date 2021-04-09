
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests

from app import app



# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing
# pytest --cov . --cov-report html



class TestBase(TestCase):   # main function to create the app environment

    def create_app(self):   # its configuration
          
        return app

       

# class TestViews(TestBase):  # This test confirms that the page loads

#     def test_home_get(self):
#         response = self.client.get(url_for('middleend'))
#         self.assertEqual(response.status_code, 200)



# class TestResponse(TestBase):

#     def test_one(self):
#     # We will mock a response of 1 and test that we get football returned.
#         with patch('requests.get') as g:
#             g.return_value.text = "Dan"

#             response = self.client.get(url_for('middleend'))
#             self.assertIn(b'Dan', response.data)