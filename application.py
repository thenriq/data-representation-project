from flask import Flask, json, url_for, request, redirect, abort,jsonify, render_template,session
from logprofileDAO import LogProfileDAO, logprofileDAO
from filmDAO import FilmDAO, filmDAO
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb.cursors
import re
import dbconfig as cfg


app = Flask(__name__, static_url_path='', static_folder='.')

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = cfg.mysql['host']
app.config['MYSQL_USER'] = cfg.mysql['user']
app.config['MYSQL_PASSWORD'] = cfg.mysql['password']
app.config['MYSQL_DB'] = cfg.mysql['database']

mysql = MySQL(app)
 
# Login page
#@app.route("/index")
@app.route('/')
def index():
    if 'loggedin' in session: 
        return render_template("index.html")
    return redirect(url_for('login'))
#app.run()

#@app.route('/')
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

# Logout
@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))

# Calls profiles page to open
@app.route("/profiles")
def profiles():
    if 'loggedin' in session: 
        return render_template("profiles.html")
    return redirect(url_for('login'))

# Calls films page to open
@app.route("/films")
def fimls():
    if 'loggedin' in session: 
        return render_template("films.html")
    return redirect(url_for('login'))

# Calls register page to open
@app.route("/register", methods =['GET', 'POST'])
def register():
    return render_template('register.html')

# Load css on page
@app.route("/profiles")
def cssfile():
    if 'loggedin' in session: 
        return render_template("profiles.html")
    return redirect(url_for('login'))



# --------- Access to DB - PROFILE --------------------------------------------------------------
# Get all - PROFILE
@app.route('/profile')
def getAll():
    return jsonify(logprofileDAO.getAll())

# Get passwd by ID
@app.route('/passwd/<int:id>')
def getPasswd(id):
    return  jsonify(logprofileDAO.getPass(id))

# find by id - PROFILE
@app.route('/profile/<int:id>')
def findById(id):
    return jsonify(logprofileDAO.findByID(id))

# Create - PROFILE
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

#UPDATE by ID: - PROFILE
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
        currentProfile['email'] = request.json['email']
    
    logprofileDAO.update(currentProfile)
  
    
    return jsonify(currentProfile)

#DELETE: - PROFILE
@app.route('/profile/<int:id>', methods=['DELETE'])
def delete(id):
    logprofileDAO.delete(id)
    
    return jsonify({"done":True})


# --------- Access to DB - FILMS ------------------------------------------------
# Get all - FILMS
@app.route('/film')
def getAllFilms():
    return jsonify(filmDAO.getAll())


# find by id - FILMS
@app.route('/film/<int:id>')
def findByIdFILM(id):
    return jsonify(filmDAO.findByID(id))


# Create - FILMS
@app.route('/film', methods=['POST'])
def createFilm():
    
    if not request.json:
        abort(400)
    
    film = {
        #"id": request.json["id"], --> for auto-increment table this will not be used
        'movie_name': request.json['movie_name'],
        'movie_gender': request.json['movie_gender'],
        'movie_year': request.json['movie_year'],
        'movie_box_office': request.json['movie_box_office']
    }
    return jsonify(filmDAO.create(film))

#UPDATE by ID: - PROFILE
@app.route('/film/<int:id>', methods=['PUT'])
def updatefilm(id):
    foundFilm = filmDAO.findByID(id)
    print(foundFilm)
    if foundFilm == {}:
        return jsonify({}), 404
    currentFilm = foundFilm
    
    if 'movie_name' in request.json:
        currentFilm['movie_name'] = request.json['movie_name']
    
    if 'movie_gender' in request.json:
       currentFilm['movie_gender'] = request.json['movie_gender']
    
    if 'movie_year' in request.json:
        currentFilm['movie_year'] = request.json['movie_year']
    
    if 'movie_box_office' in request.json:
        currentFilm['movie_box_office'] = request.json['movie_box_office']
    
    filmDAO.update(currentFilm)
  
    
    return jsonify(currentFilm)


#DELETE: - FILM
@app.route('/film/<int:id>', methods=['DELETE'])
def deleteFilm(id):
    filmDAO.delete(id)
    
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug=True)