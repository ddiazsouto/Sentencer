from flask import Flask, render_template
app = Flask(__name__)

@app.route('/number', methods=['GET'])
def number():
    template='main.html'
    return render_template(template, title='Frontend')

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)