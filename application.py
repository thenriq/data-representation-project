#!flask/bin/python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'your secret key'
  
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'datarepresentation'

mysql = MySQL(app)

#@app.route('/')

#def index():
#    return redirect(url_for('start'))

#@app.route('/start')
#def start():
    #return "Hello, World! This is changed"
#    return render_template('index.html')

# Creating login for application
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM loginprofile WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)



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