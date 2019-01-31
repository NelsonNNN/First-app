from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.secret_key = 'nelliville'
# app.database = 'trial.db'
# app.database = 'table2.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create sqlalchemy object
db = SQLAlchemy(app)
from SQLalch import *

def need_to_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in first')
            return redirect(url_for('login'))
    return wrap
@app.route('/')
@need_to_login
def home():
    # g.db = database_conn()
    # cur = g.db.execute('select * from titles')
    # posts = [dict(title=row[1], description=row[0]) for row in cur.fetchall()]
    # g.db.close()
    #return 'Hello, Flask!'
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts = posts)

@app.route('/welcome')
def welcome():
    # g.db = table_conn()
    # pos = g.db.execute('select * from table3')
    # reads = (dict(title=row[1], description=row[2]) for row in pos.fetchall())
    return render_template('welcome.html')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] !='admin':
            return 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route('/logout')
@need_to_login
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('welcome'))

# def database_conn():
#     return sqlite3.connect("titles.db")

# def table_conn():
#     return sqlite3.connect(app.database)

if __name__ == ('__main__'):
    app.run(debug = True)
