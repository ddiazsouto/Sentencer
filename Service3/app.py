from flask import Flask, jsonify
from elementae import azar, expresser
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomization():

    mood = azar([0, 1], 1)
    output = expresser(mood)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)
