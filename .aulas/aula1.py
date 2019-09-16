"""Apliacação web com flask - Básica.v1
"""
from flask import Flask

app = Flask(__name__)

@app.route('/index.jsp')
@app.route('/')
def home():
    return 'HELLO WORLD! aplicaçao web'

if __name__ == "__main__":
    app.run()
             