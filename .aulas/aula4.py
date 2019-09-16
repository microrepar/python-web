"""Apliacação web com flask - Básica.v3
Modo Debug ativado
Definindo porta de comunicação para aplicação
Permitindo o acesso de outros dispositivos da rede
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'HELLO WORLD!'


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
           