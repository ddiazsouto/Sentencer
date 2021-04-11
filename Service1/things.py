from os import getenv
import pymysql



login = getenv('PASSWD')


def callme(msg):
    DanSQL('master').write("CREATE TABLE IF NOT EXISTS some(Date TIMESTAMP DEFAULT now(), Sentence VARCHAR(100), id INT NOT NULL AUTO_INCREMENT PRIMARY KEY);")
    DanSQL('master').write(f"INSERT INTO some(Sentence) values('{msg}');")



class DanSQL():

    def __init__(self, dabase):

        self.Make = pymysql.connect(host='34.121.192.21', user='root', passwd=login, db=dabase)
        self.MySQL = self.Make.cursor()
        self.db = dabase


    def sudo(self):
        self.Make.commit()


    def write(self, str):
        init=DanSQL(self.db)

        init.MySQL.execute(str)
        init.sudo()
        init.off()      
        

    def get(self, str):

        init=DanSQL(self.db)

        init.MySQL.execute(str)
        out = init.MySQL.fetchall()
        init.off()
        return out


    def off(self):
       
        self.Make.close()
        self.MySQL.close()

