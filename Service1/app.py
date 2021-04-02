from flask import Flask
app = Flask(__name__)

@app.route('/number', methods=['GET'])
def number():
    return 1

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0' debug=True)