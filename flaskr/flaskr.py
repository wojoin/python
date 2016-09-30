# -*- coding: utf-8 -*-
# Project Name  : Python 
# File Name     : flaskr.py
# Author        : 细嗅蔷薇
# Date Time     : 2016/9/27 17:36
# Description   :
# Version       : 1.0.1

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create our little application :)
app = Flask(__name__)

print("默认配置","*"*50)
for key,value in app.config.items():
    print(key,":\t",value)

app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# 更改app.config之后的配置
print("更改之后的配置","*"*50)
for key,value in app.config.items():
    print(key,":\t",value)

# set FLASK_APP=flaskr
# set FLASK_DEBUG=1
# flask run

def connect_db():
    """Connects to the specific database."""
    row = sqlite3.connect(app.config['DATABASE'])
    row.row_factory = sqlite3.Row
    return row


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


# create a function and hook it into the Flask command that initializes the database.
# app.cli.command('initdb') registers a new command with the flask script

@app.cli.command('initdb')
def initdb_command():
    """Initializes the databse."""
    init_db()
    print("Initialized the databse.")


def get_db():
    """Opens a new database connection if there is none yet
    for the current application context."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Close the database again aat the end of he request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Step 5: The View Function
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title,text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'],request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))



# app.run() 加上即可运行flaskr项目
















