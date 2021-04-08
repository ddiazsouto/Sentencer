from flask import Flask, request, jsonify
from random import randint
from frasium import binary, azar
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomizer():

    output = dict()

    randlist = azar([1, 10], 4)    
    dark = binary()

    output['dark'] = dark
    output['list'] = randlist

    return jsonify(output)



if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)