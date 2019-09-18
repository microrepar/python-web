from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return redirect(url_for('curriculo'))


@app.route('/curriculo')
def curriculo():
    return render_template('index.html')


