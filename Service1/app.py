from flask import Flask, render_template, request, Response, jsonify, url_for
from things import DanSQL
app = Flask(__name__)
import requests
from os import getenv



@app.route('/', methods=['GET', 'POST'])
def main():

    # host = getenv("HOSTNAME") 

    msg = 'Click in New Message to Start the fun!!'
    color = '000000'


    if request.method == 'GET':
        gotit = requests.get('http://10.128.0.54:5050/').json()   
        color = gotit['color']
        msg = gotit['sentence']



    
    
    if request.method == 'POST':

        DanSQL().write("CREATE TABLE IF NOT EXISTS some(Date TIMESTAMP DEFAULT now(), Sentence VARCHAR(100), id INT NOT NULL AUTO_INCREMENT PRIMARY KEY);")
        DanSQL().write("INSERT INTO some(data, more) VALUES(000, 987);")



    return render_template('main.html', title='Frontend', color=color, var=msg)

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)