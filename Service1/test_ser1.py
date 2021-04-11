
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from things import DanSQL

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
        response = self.client.get(url_for('main'))
        self.assertEqual(response.status_code, 200)

    def test_data_get(self):
        response = self.client.get(url_for('data'))
        self.assertEqual(response.status_code, 200)




class MyAlchemy():

    def connects():

        try:
            attempt = DanSQL('mysql')
            attempt.off()
            return True
        
        except: return False
               

    def creates(value):

                
        DanSQL('master').write('CREATE DATABASE IF NOT EXISTS testbase;')      

        DanSQL('testbase').write('CREATE TABLE IF NOT EXISTS Test(column1 VARCHAR(10));')
        DanSQL('testbase').write(f'INSERT INTO Test(column1) values({str(value)});')        
        var = DanSQL('testbase').get('SELECT * FROM Test;')

        DanSQL('master').write('DROP DATABASE testbase;')

        

        return str(var)    




def test4():                            # Is the conection with the database successful ?
    assert MyAlchemy.connects() == True

def test5():                            # Checks that the object can interact with the database using an integer
    assert '127' in MyAlchemy.creates(127)

def test6():                            # Checks that the object can interact with the database using a string
    assert 'Dan' in MyAlchemy.creates("'Dan'")





# class TestResponse(TestBase):

    # def test_one(self):
    # # We will mock a response of 1 and test that we get football returned.
    #     with patch('requests.get') as g:

    #         g.return_value = 'dasdd'
    #         response = self.client.get(url_for('main'))           
            
    #         self.assertIn(b'Dan', response.data)