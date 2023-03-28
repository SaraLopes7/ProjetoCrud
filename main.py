from flask import Flask, Response, request
from app.models import User
from flask_login import login_user, logout_user, current_user
from flask import render_template, redirect, url_for, flash
import mysql.connector 
import json

# LOGIN
@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form['login'].upper()
        senha= request.form['senha'].upper()

    return render_template("Login/login.html")

# CADASTRO 
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form['nome'].upper()
        email = request.form['email']
        usuario = request.form['login']
        senha = request.form['senha']

    return render_template("Cadastro/cadastro.html")

# PÁGINA DE OPÇÕES
@app.route("/opcoes", methods=["GET"])
def opcoes():
    return render_template("Opcoes/opcoes.html")

# PÁGINA DE CRIAR
@app.route("/create", methods=["POST"])
def create():

    if request.method == "POST":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes']

    return render_template("Create/create.html")

# PÁGINA DE LER 
@app.route("/read", methods=["GET"])
def read():

    if request.method == "GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes']

    return render_template("Read/read.html")

# PÁGINA DE ATUALIZAR 
@app.route("/update", methods=["GET", "POST"])
def update():

    if request.method == "POST, GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()

    return render_template("Update/update.html")

# PÁGINA DE DELETAR 
@app.route("/delete", methods=["GET"])
def deletar():

    if request.method == "GET":
        nome = request.form['nome'].upper()
        autor = request.form['autor'].upper()
        genero = request.form['genero'].upper()
        Tpaginas = request.form['Tpaginas']
        Lpaginas = request.form['Lpaginas']
        anotacoes = request.form['anotacoes'].upper()

    return render_template("Delete/delete.html")

app.run(debug=True)