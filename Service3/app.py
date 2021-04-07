from flask import Flask
from random import randint
from Service4.elementae import azar
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomization():
    sentences = ['It was the craziest thing that my eyes have seen', 'How great', 'Could be better', 'Holly Cow!!', \
    'Awesome', 'Like a fish in the water', 'Who cares?', 'Yeeah baby!!', 'Not bad at all', 'Fantastic!', 'Nice!']

    select = randint(0, 10)

    return str(sentences[select])

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)