
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

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



