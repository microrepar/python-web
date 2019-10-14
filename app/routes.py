from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/page_404')
def page_404():
    return render_template('page_404.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/login')
def login():
    return render_template('login.html')


