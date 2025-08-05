from app import app
from flask import render_template, url_for
from flask import request


@app.route("/")
def homepage():
    context = {"nome": "Alex", "idade": 25}
    lista = [10, 20, 30]
    return render_template("index.html", context=context, teste=lista[0])


@app.route("/contato/", methods=["GET", "POST"])
def contato():
    context = {}
    if request.method == "GET":
        pesquisa = request.args.get("pesquisa")
        context.update({"pesquisa": pesquisa})
        print("GET:", pesquisa)
    if request.method == "POST":
        pesquisa = request.form["pesquisa"]
        print("POST:", pesquisa)
    return render_template("contato.html", context=context)


