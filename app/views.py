from app import app
from app import db
from app.models import Contato
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
        # salvando os dados que o usuário vai mandar
        nome = request.form["nome"]
        email = request.form["email"]
        assunto = request.form["assunto"]
        mensagem = request.form["mensagem"]
        # data_time = request.form["year"]

        # criando o objeto do contato
        contato = Contato(nome=nome, email=email, assunto=assunto, mensagem=mensagem)

        # add os dados no banco e fazendo o commit
        db.session.add(contato)
        db.session.commit()
        # print("POST:", pesquisa)
    return render_template("contato.html", context=context)
