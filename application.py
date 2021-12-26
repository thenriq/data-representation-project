#!flask/bin/python
from flask.helpers import url_for,  request
from flask import Flask, redirect, render_template

app = Flask(__name__, static_url_path='', static_folder='.', template_folder='templates_folder')

@app.route('/')
def index():
    return redirect(url_for('start'))

@app.route('/start')
def start():
    #return "Hello, World! This is changed"
    return render_template('index.html')


@app.route('/book/<int:id>')
def getBook(id):
    return "you want book with " + str(id)

if __name__ == '__main__' :
    app.run(debug = True)