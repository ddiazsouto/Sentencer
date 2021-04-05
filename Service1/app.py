from flask import Flask, render_template, request, Response, jsonify, url_for
app = Flask(__name__)
import requests

some={'dan':'Cool', 'Other': 'not so cool'}


@app.route('/', methods=['GET', 'POST'])
def main():
    template='main.html'
    color='blue'

    parsed = requests.get('http://10.128.0.54:5050/').text
    

    if request.method == 'POST':

        data_received = request.data.decode('utf-8')      
        return Response(data_received)

    return render_template(template, title='Frontend', color=color, var=parsed)

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)