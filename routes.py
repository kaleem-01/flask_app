import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask import render_template, request, redirect, g


#Connect to database
# con = sql.connect('instance/test.db')
# con.execute('CREATE TABLE IF NOT EXISTS tbl_data (ID INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT)')
# con.close

@app.route('/', methods = ['POST','GET'])
def index():
    # Show the form when entering the website
    if request.method == 'GET':
        return render_template('index.html')
    else:   # If the form is submitted (i.e. request.method == POST)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        name = first_name + last_name
        try:
        # # Add track_var
        # # g.track_var['name'] = name
        # con = sql.connect('instance/test.db')
        # c = con.cursor() # Cursor
        # # Add visitor data
        # c.execute('INSERT INTO flask_usage (username) VALUES (?)', [name])
        # con.commit() # Save visitor detail
            return redirect('/homepage')
        except: # Fix exception later
            return 'woops'

@app.route('/homepage', methods = ['POST', 'GET'])
def homepage():
    return render_template('index.html')

@app.route('/learn_more', methods = ['POST', 'GET'])
def learn_more():
    return render_template('learn_more.html')

@app.route('/learn_more_b', methods = ['POST', 'GET'])
def learn_more_b():
    return render_template('learn_more_b.html')


@app.route('/confirmation', methods = ['POST', 'GET'])
def confirmation():
    return render_template('done.html')


@app.route('/confirmation_b', methods = ['POST', 'GET'])
def confirmation_b():
    return render_template('done_b.html')


@app.route('/website_b', methods = ['POST','GET'])
def website_b():
    return render_template('website_b.html')
