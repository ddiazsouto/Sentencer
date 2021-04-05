from flask import Flask, render_template, request, Response, jsonify
import requests
app = Flask(__name__)

some={'dan':'Cool', 'Other': 'not so cool'}


@app.route('/', methods=['GET', 'POST'])
def middleend():

    response = requests.get('http://35.223.236.160:5000/')

    # if request.method == 'POST':

    #     data_received = request.data.decode('utf-8')      
    #     return Response(data_received)

    return f'Hey, I am talking with Service 2, and its saying: {response.text}'

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0', debug=True)