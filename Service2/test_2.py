
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from frasium import phraser
import pytest
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
        response = self.client.get(url_for('randomizer'))
        self.assertEqual(response.status_code, 200)


def testing_first():    
    assert str(phraser([1, 2, 3, 4], 1)) == "{'pronoun': 'you', 'verb1': 'stay', 'verb2': 'skipping', 'preposition': 'in', 'aux': 'Do'}"

def testing_second():
    assert str(phraser([2, 3, 4, 5], 1)) == "{'pronoun': 'he', 'verb1': 'get', 'verb2': 'pointing', 'preposition': 'a', 'aux': 'Does'}"

def testing_third():
    assert str(phraser([1, 2, 3, 4], 0)) == "{'pronoun': 'You', 'verb1': 'stay', 'verb2': 'skipping', 'preposition': 'in'}"

def testing_fourth():
    assert str(phraser([2, 3, 4, 5], 0)) == "{'pronoun': 'He', 'verb1': 'gets', 'verb2': 'pointing', 'preposition': 'a'}"


# class TestResponse(TestBase):

#     def test_one(self):
#     # We will mock a response of 1 and test that we get football returned.
#         with patch('requests.get') as g:
#             g.return_value.text = "Dan"

#             response = self.client.get(url_for('middleend'))
#             self.assertIn(b'dan.html', response.data)