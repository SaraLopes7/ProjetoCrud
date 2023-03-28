from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(id_usuario):
    db.mycursor.execute("SELECT * FROM Usuarios WHERE Id = %s", [id_usuario])
    return db.mycursor.fetchall()

class db_livraria(db.Model):
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


def inserirlivros(self):
    Values = (self.id_usuario, self.nome_livro, self.autor, self.genero, self.totalPginas, self.paginasLidas, self.anotacoes)
    db.mycursor.execute("INSERT INTO tbl_livros VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)", Values)
    db.db.commit()

def deletarlivros(self):
    db = f"DELETE * FROM tbl_livros WHERE nome_livro ='{self.nome_livro}'"
    db.db.commit()

def atualizarlivros(self):
    db = f"UPDATE * FROM tbl_livros WHERE nome_livro ='{self.nome_livro}'" 
    db.db.commit()

def cadastro(self):
    Values = (self.nomep, self.Email, self.usuario, self.senha)
    db.mycursor.execute("INSERT INTO usuario VALUES (%s, %s, %s, %s)", Values)
    db.db.commit()