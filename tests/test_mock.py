
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from Service4 import app



# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing
# pytest --cov . --cov-report html


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_one(self):
    # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            g.return_value.text = "Dan"

            response = self.client.get(url_for('frontend'))
            self.assertIn(b'dan.html', response.data)