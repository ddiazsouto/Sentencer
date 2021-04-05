from flask import Flask, render_template, request, Response, jsonify, url_for
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def middleend():

    output = dict()

    response = requests.get('http://10.128.0.54:5000/')  #  Service 2
    sentence = requests.get('http://35.223.236.160:5005/')  #  Service 3

    output[response.text] = sentence.text



    # if request.method == 'POST':

    #     data_received = request.data.decode('utf-8')      
    #     return Response(data_received)

    return f'{output}'

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0', debug=True)