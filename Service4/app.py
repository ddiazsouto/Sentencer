from flask import Flask
app = Flask(__name__)

@app.route('/number', methods=['GET'])
def number():
    return 4

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0', debug=True)