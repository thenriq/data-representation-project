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

@app.route('/user')
def getUser():
    return "served by getUser"

@app.route('/user/<int:id>')
def findByIdUser(id):
    return "served by findByUser with id = "+str(id)

@app.route("/demo_url_for/")
def demoUrlFor():
    returnString = "url For index is " + url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser " + url_for('findByIdUser', id=12)
    return returnString

@app.route("/demo_request", methods=['POST', 'GET', 'DELETE', 'PUT'])
def demoRequest():
    returnString = "The chosen option is " + request.method 
    return returnString


if __name__ == '__main__' :
    app.run(debug = True)