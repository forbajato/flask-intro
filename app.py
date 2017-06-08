#################
#### Imports ####
#################

from flask import Flask, render_template, redirect, url_for, request, session,\
 flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os

app = Flask(__name__)

# config
# before starting the server you need to define an environment variable
# APP_SETTINGS and set it equal to one of the classes in config.py.
# for example: export APP_SETTINGS="config.DevelopmentConfig" if you want
# to use the development configuration.

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# Import models after you create the SQLAlchemy object! - reference models.py -
# you import the database there (as db), thus you can't import BlogPost here
# before you define db.

from models import *
from project.users.views import users_blueprint


# register our blueprints
app.register_blueprint(users_blueprint)


##########################
#### helper functions ####
##########################


# Makes you login before you do certain things on the site
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password']\
#          != 'admin':
#             error = 'Invalid credentials.  Please try again.'
#         else:
#             session['logged_in'] = True
#             flash("You were just logged in")
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     session.pop('logged_in', None)
#     flash("You were just logged out")
#     return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
