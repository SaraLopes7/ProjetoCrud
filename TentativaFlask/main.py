from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQLdb
import mysql.connector
import json 

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = 'CHAVE'
"""
db = mysql.connector.connect( host="localhost",
                              user="root",
                              password="lopesSara7#",
                              database="db_livraria"
)

mycursor = db.cursor()
"""
#app = Flask(__name__, template_folder='templates')
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'lopesSara7#'
#app.config['MYSQL_DB'] = 'db_livraria'

#db = MySQLdb(app)

# mycursor = db.connection.cursor()

class db_livraria():
    def __init__(self, id_usuario, nome_usuario, email, usuario, senha, id_livros, nome_livro, autor, genero, totalPginas, paginasLidas, anotacoes):   
        # cadastro usuario
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email = email
        self.usuario = usuario
        self.senha = senha
        
        # cadastro livro
        self.id_livros = id_livros
        self.nome_livro = nome_livro
        self.autor = autor
        self.genero = genero
        self.totalPginas = totalPginas
        self.paginasLidas = paginasLidas
        self.anotacoes = anotacoes

# LOGIN
@app.route("/", methods=["GET"])
def inicial():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    user = request.form['user']
    senha= request.form['senha']
    print(user)
    print(senha)

    db = mysql.connector.connect(host="localhost", user="root", password="lopesSara7#", database="db_livraria")
    cont = 0
    if db.is_connected():
        print("CONECTADO")
        mycursor = db.cursor()
        mycursor.execute("SELECT usuario, senha FROM tbl_cadastros;")

        usuariosBD = mycursor.fetchall()

        for usuario in usuariosBD:
            cont += 1
            usuarioNome = str(usuario[0])
            usuarioSenha = str(usuario[1])
    
    if usuarioNome == user and usuarioSenha == senha:
        return render_template("opcoes.html")
    
    if cont >= len(usuariosBD):
        flash("Usuário não cadastrado!")
        return render_template("cadastro.html")

# CADASTRO 
@app.route("/cadastro", methods=["POST"])
def cadastro(self):

    nome = request.form['nome']
    email = request.form['email']
    user = request.form['user']
    senha = request.form['senha']
    print(nome)
    print(email)
    print(user)
    print(senha)

    db = mysql.connector.connect(host="localhost", user="root", password="lopesSara7#", database="db_livraria")
    if db.is_connected():
        print("CONECTADO")
        mycursor = db.cursor()
        # Values = (self.id_usuario, self.nome_usuario, self.email, self.usuario, self.senha)
        mycursor.execute("INSERT INTO tbl_cadastros VALUES (DEFAULT, '{nome}', '{email}', '{user}', '{senha}');")
        db.commit()

    if db.is_connected:
        mycursor.close()
        db.close()
    
    return render_template("cadastro.html")

# PÁGINA DE OPÇÕES
@app.route("/opcoes", methods=["GET"])
def opcoes():
    db = mysql.connector.connect(host="localhost", user="root", password="lopesSara7#", database="db_livraria")

    if db.is_connected():
        print("CONECTADO")
        mycursor = db.cursor()
        mycursor.execute("SELECT usuario FROM tbl_cadastros;")

        usuario = mycursor.fetchall()
    return render_template("opcoes.html", usuario=usuario)

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

    return render_template("create.html")

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

    return render_template("read.html")

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

# Com esse if não precisa ficar executando o main no terminal
if __name__ in "__main__":
    app.run(debug=True)

