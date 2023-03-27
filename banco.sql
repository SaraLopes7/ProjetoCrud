CREATE DATABASE db_livraria;

CREATE TABLE tbl_cadastros (
    id_usuario MEDIUMINT PRIMARY KEY,
    nome VARCHAR(60),
    email VARCHAR(45) UNIQUE NOT NULL,
    usuario VARCHAR(8) UNIQUE NOT NULL PRIMARY KEY,
    senha VARCHAR(15) NOT NULL
);

CREATE TABLE tbl_livros (
    id_livros MEDIUMINT PRIMARY KEY,
    nome VARCHAR(60),
    autor VARCHAR(60),
    genero VARCHAR(30),
    totalPaginas INT(5.000),
    paginasLidas INT(5.000),
    anotacoes VARCHAR(500),
);