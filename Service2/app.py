from flask import Flask, request, jsonify
from random import randint
from frasium import binary, azar, phraser
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomizer():

    output = dict()

    randlist = azar([0, 7], 4)    
    dark = binary()
    question = binary()

    output['dark'] = dark
    output['list'] = randlist

    check = phraser(randlist, question)

    return jsonify(check)



if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)