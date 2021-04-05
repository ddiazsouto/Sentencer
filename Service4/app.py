from flask import Flask, render_template, request, Response, jsonify
app = Flask(__name__)

some={'dan':'Cool', 'Other': 'not so cool'}


@app.route('/', methods=['GET', 'POST'])
def middleend():
    template='main.html'
    color='red'


    if request.method == 'POST':

        data_received = request.data.decode('utf-8')      
        return Response(data_received)

    return f"<body style='background-color:{color};'"

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0', debug=True)