
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import pytest
from elementae import expresser, azar

from app import app



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
        response = self.client.get(url_for('randomization'))
        self.assertEqual(response.status_code, 200)




def testing_first():    
    assert 'expression' in str(expresser(1))

def testing_second():    
    assert 'mood' in str(expresser(1))

def testing_third():    
    assert 'mood' in str(expresser(0))

def testing_fourth():    
    assert 'expression' in str(expresser(0))

