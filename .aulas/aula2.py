"""Apliacação web com flask - Básica.v2
Modo Debug ativado
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index.php')
def home():
    return 'HELLO WORLD!'


if __name__ == "__main__":
    app.run(debug=True)
