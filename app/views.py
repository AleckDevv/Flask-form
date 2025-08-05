from app import app
from flask import render_template, url_for


""" @app.route("/")
def homepage():
    nome = "Alex"
    idade = 25
    return render_template("index.html", nome=nome, idade=idade) """


@app.route("/")
def homepage():
    context = {"nome": "Alex", "idade": 25}
    lista = [10, 20, 30]
    return render_template("index.html", context=context, teste=lista[0])


@app.route("/sobre/")
def sobre():
    return render_template("sobre.html")


