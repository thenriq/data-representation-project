from flask import Flask, json, url_for, request, redirect, abort,jsonify
from logprofileDAO import LogProfileDAO, logprofileDAO
import re

app = Flask(__name__, static_url_path='', static_folder='staticpages')

app.secret_key = 'your secret key'
  
  
# Creating login for application
@app.route('/')
def index():
    return "hello GMIT"


# Get all
@app.route('/profile')
def getAll():
    return jsonify(logprofileDAO.getAll())

# find by id
@app.route('/profile/<int:id>')
def findById(id):
    return jsonify(logprofileDAO.findByID(id))

# Create
@app.route('/profile', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    profile = {
        #"id": request.json["id"], --> for auto-increment table this will not be used
        "username": request.json["username"],
        "password": request.json["password"],
        "email": request.json["email"]
    }
    return jsonify(logprofileDAO.create(profile))

#UPDATE by ID:
@app.route('/profile/<int:id>', methods=['PUT'])
def update(id):
    foundProfile = logprofileDAO.findByID(id)
    print(foundProfile)
    if foundProfile == {}:
        return jsonify({}), 404
    currentProfile = foundProfile
    
    if 'username' in request.json:
        currentProfile['username'] = request.json['username']
    
    if 'password' in request.json:
        currentProfile['password'] = request.json['password']
    
    if 'email' in request.json:
        currentProfile['email'] = request.json['premailce']
    
    logprofileDAO.update(currentProfile)
  
    
    return jsonify(currentProfile)

#DELETE:
@app.route('/profile/<int:id>', methods=['DELETE'])
def delete(id):
    logprofileDAO.delete(id)
    
    return jsonify({"done":True})



#@app.route('/login', methods =['GET', 'POST'])
#def login():
#    msg = ''
#    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#        username = request.form['username']
#        password = request.form['password']
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute('SELECT * FROM loginprofile WHERE username = % s AND password = % s', (username, password, ))
#        account = cursor.fetchone()
#        if account:
#            session['loggedin'] = True
#            session['id'] = account['id']
#            session['username'] = account['username']
#            msg = 'Logged in successfully !'
#            return render_template('index.html', msg = msg)
#        else:
#            msg = 'Incorrect username / password !'
#    return render_template('login.html', msg = msg)



#@app.route('/book/<int:id>')
#def getBook(id):
#    return "you want book with " + str(id)

#@app.route('/user')
#def getUser():
#    return "served by getUser"

#@app.route('/user/<int:id>')
#def findByIdUser(id):
#    return "served by findByUser with id = "+str(id)

#@app.route("/demo_url_for/")
#def demoUrlFor():
#    returnString = "url For index is " + url_for('index')
#    returnString += "<br/>"
#    returnString += "url for findByIdUser " + url_for('findByIdUser', id=12)
#    return returnString

#@app.route("/demo_request", methods=['POST', 'GET', 'DELETE', 'PUT'])
#def demoRequest():
#    returnString = "The chosen option is " + request.method 
#    return returnString


if __name__ == '__main__' :
    app.run(debug = True)