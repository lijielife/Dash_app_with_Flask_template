# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 02:04:00 2018

@author: jimmybow
"""

from flask import Flask, render_template, request
import Dash_App1, Dash_App2

app = Flask(__name__)
app, create_secret = Dash_App1.Add_Dash(app)
app = Dash_App2.Add_Dash(app)

@app.route('/')
def expressions():
    var1 = "variable1"
    list1 = [1, 2, 3, 4]
    dict1 = {1: "1", 2: "2", 3: "3"}
    dash_url = '/dash?secret={}'.format(create_secret('secret'))
    return render_template('expression.html', var1=var1, list1=list1, dict1=dict1, dash_url=dash_url)

@app.route('/user/<int:user_id>')
def get_user(user_id):
    return "User ID: %d" % user_id

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        return "Hello World"
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

@app.route('/statements')
def statements():
    var1 = "variable1"
    list1 = [1, 2, 3, 4]
    return render_template('statements.html', var1=var1, list1=list1)

if __name__ == '__main__':
    app.run()