
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

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


# class TestResponse(TestBase):

#     def test_one(self): 

#         with patch('random.randint') as a:                #  We mock the function color, which is of random nature
#             value = 1                                  
#             a.return_value.data = 1                                 #  it should return this output                                                                      
#             response = self.client.get(url_for('randomization'))
#             self.assertIn(b'9a0000', response.data)
