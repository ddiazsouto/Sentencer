from flask import Flask, render_template, request, Response, jsonify, url_for
from things import DanSQL
app = Flask(__name__)
import requests
from os import getenv



@app.route('/', methods=['GET', 'POST'])
def main():
    template='main.html'

    # host = getenv("HOSTNAME")    

    # DanSQL().write("CREATE TABLE IF NOT EXISTS some(data int(10), more int(20));")

    #DanSQL().write("INSERT INTO some(data, more) VALUES(1234, 7895);")
    
    if request.method == 'GET':
        gotit = requests.get('http://10.128.0.54:5050/').json()
    

    if request.method == 'POST':

        msg = 'POST READ'

    color = gotit['color']
    msg = gotit['sentence']
    

    return render_template(template, title='Frontend', color=color, var=msg)

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)