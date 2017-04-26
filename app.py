from flask import Flask, render_template, redirect, url_for, request, session, flash 
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# import sqlite3

app = Flask(__name__)

#This is really dangeroius
# key should be random
# key should be placed in a separate file, added with imports
app.secret_key = 'my precious'

# app.database = "sample.db"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'

db = SQLAlchemy(app)

# Import models after you create the SQLAlchemy object! - reference models.py - you import the database there (as db), thus you can't import BlogPost here before you define db.

from models import *

# Makes you login before you do certain things on the site
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
    #g.db = connect_db()
    #cur = g.db.execute('select * from posts')
    #posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    #g.db.close()
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials.  Please try again.'
        else:
            session['logged_in'] = True
            flash("You were just logged in")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/logout")
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You were just logged out")
    return redirect(url_for('welcome'))

# def connect_db():
#    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
