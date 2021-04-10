
from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
import requests

from app import app, middleend
from blogic import BeLogic



# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing
# pytest --cov . --cov-report html



class TestBase(TestCase):   # main function to create the app environment

    def create_app(self):   # its configuration
          
        return app

       

class TestViews(TestBase):  # This test confirms that the page loads

    def test_home_get(self):
        response = self.client.get(url_for('middleend'))
        self.assertEqual(response.status_code, 200)



class TestResponse(TestBase):

    def test_one(self): 

        with patch('blogic.BeLogic.color') as a:                #  We mock the function color, which is of random nature
            value = '9a0000'                                         #     and we obtain the output of the page
            a.return_value = value                                 #  it should return this output                                                                      
            response = eval(self.client.get(url_for('middleend')).data.decode('utf-8')[:-1])
            response = response['color']
            self.assertIn('9a0000', response)


    def test_two(self): 

        with patch('blogic.BeLogic.talk') as a:             # We mock the talk function to check if it is

            a.return_value = 'Just a simple test? It works!'       #  returned at the url
            response = self.client.get(url_for('middleend'))
            self.assertIn(b'Just a simple test? It works!', response.data)