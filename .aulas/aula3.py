"""Apliacação web com flask - Básica.v3
Modo Debug ativado
Definindo porta de comunicação para aplicação
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/teste.xyz')
def home():
    return 'HELLO WORLD!'


if __name__ == "__main__":
    app.run(debug=True, port=8080)
