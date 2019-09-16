from app import app
from flask import render_template

@app.route('/')
def home():
    return 'HELLO WORLD'


@app.route('/curriculo')
def curriculo():
    return render_template('index.html')


