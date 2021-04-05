from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomization():
    sentences = ['How great', 'Could be better', 'Holly Cow!!', 'Awesome', 'Like a fish in the water', 'Who cares?']

    select = randint(0, 6)

    return str(sentences[select])

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)