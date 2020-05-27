from flask import Flask, render_template, request, session 
from random import choice
from Banda import *


app = Flask(__name__)
@app.route('/')
def presentacion():
    return render_template("preparar.html")

@app.route('/banda')

def index():
    banda = Banda()
    numeromusicos = randint(5,10)
    b = banda.crearBanda(numeromusicos)
    return render_template("index.html", b=b, n=numeromusicos)


if __name__ == '__main__':
   app.run(debug = True)