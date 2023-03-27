from app import db, login_manager
from flask_login import UserMixin

def get_user(CPF):
db.mycursor.execute("SELECT * FROM Usuarios WHERE CPF = %s", [CPF])
return db.mycursor.fetchall()

class User(UserMixin):


def __init__(self, Nome, Autor, Genero, Paginas, Lidas, NomePessoa, Email, usuario, senha):
    # cadastro livro
    self.Nomeliv = Nome
    self.NomeAutorliv = Autor
    self.generoliv = Genero
    self.TotalPagliv = Paginas
    self.paginaslidasliv = Lidas
    self.paginasRest = self.TotalPagliv - self.paginaslidasliv

    # cadastro pessoa
    self.nomep = NomePessoa
    self.Email = Email
    self.usuario = usuario
    self.senha = senha

def inserirlivros(self):
    Values = (self.Nomeliv, self.NomeAutorliv, self.generoliv, self.TotalPagliv, self.paginaslidasliv)
    db.mycursor.execute("INSERT INTO Livros VALUES (%s, %s, %s, %s, %s, NULL)", Values)
    db.db.commit()

def deletarlivros(self):
    db = f"DELETE * FROM livros WHERE nomeliv ='{self.Nomeliv}'" # define o que será feito na tabela funcionário
    db.db.commit()

def atualizarlivros(self):
    db = f"Update * FROM livros WHERE nomeliv ='{self.Nomeliv}'" # define o que será feito na tabela funcionário
    db.db.commit() # comando que jogo os dados para o banco de dados

@staticmethod
def BuscarLivroPorNome(self):
    db.mycursor.execute("SELECT * FROM livros WHERE Nomeliv = %s", [self.Nomeliv])
    return db.mycursor.fetchone()

def cadastro(self):
    Values = (self.nomep, self.Email, self.usuario, self.senha)
    db.mycursor.execute("INSERT INTO usuario VALUES (%s, %s, %s, %s)", Values)
    db.db.commit()