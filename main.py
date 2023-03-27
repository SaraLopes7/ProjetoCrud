from app import app
import json
from app.models import User, CartaoDeCredito
from flask_login import login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash

@app.route("/index", methods=["GET"])
@app.route("/", methods=["GET"])

def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def inserir():

    if request.method == "POST":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()


    return render_template("")

@app.route("/read", methods=["GET"])
def visualizar():

    if request.method == "GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()


    return render_template("")

@app.route("/update", methods=["POST, GET"])
def atualizar():

    if request.method == "POST, GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()

    return render_template("")

@app.route("/delete", methods=["GET"])
def deletar():

    if request.method == "GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()

    return render_template("")


@app.route("/cadastro", methods=["POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form['nome'].upper()
        email = request.form['email']
        usuario = request.form['usuario']
        senha = request.form['senha']

@app.route("/delete", methods=["POST"])
def login():

    if request.method == "POST":
        usuario = request.form['usuario'].upper()
        senha= request.form['senha'].upper()

    return render_template("")



app.run(debug=True)