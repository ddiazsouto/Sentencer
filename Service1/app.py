from flask import Flask, render_template, request, Response, jsonify, url_for
from things import DanSQL, callme
app = Flask(__name__)
import requests
from os import getenv


environmental = []


@app.route('/', methods=['GET', 'POST'])
def main():

    # host = getenv("HOSTNAME")   
    
    if request.method == 'POST':
         
        msg = environmental.pop()      
        DanSQL('master').write("CREATE TABLE IF NOT EXISTS some(Date TIMESTAMP DEFAULT now(), Sentence VARCHAR(100), id INT NOT NULL AUTO_INCREMENT PRIMARY KEY);")
        DanSQL('master').write(f"INSERT INTO some(Sentence) values('{msg}');")

    
    gotit = requests.get('http://10.128.0.54:5050/').json()   
    color = gotit['color']
    msg = gotit['sentence']
    
    environmental.append(msg)
  
    return render_template('main.html', title='Frontend', color=color, var=msg)


@app.route('/data', methods=['GET', 'POST'])
def data():
    return render_template('data.html', title='data', list=DanSQL('master').get("SELECT * from some"))


if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)