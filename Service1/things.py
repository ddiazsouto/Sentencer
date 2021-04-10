from os import getenv
import pymysql


logino = getenv('DATABASE_CREDENTIALS')
login = '645202398'



class DanSQL():

    def __init__(self):

        self.Make = pymysql.connect(host='34.121.192.21', user='root', passwd=f'{login}, db='master')
        self.MySQL = self.Make.cursor()


    def sudo(self):
        self.Make.commit()


    def write(self, str):
        init=DanSQL()

        init.MySQL.execute(str)
        init.sudo()
        init.off()      
        

    def get(self, str):

        init=DanSQL()

        init.MySQL.execute(str)
        out = init.MySQL.fetchall()
        init.off()
        return out


    def off(self):
       
        self.Make.close()
        self.MySQL.close()

