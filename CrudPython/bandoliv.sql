create database APP;

use APP;

create table livro(
	titulo varchar(150) not null primary key,
    autor varchar(100) not null,
    genero varchar(100) not null,
    tpaginas int not null,
    lpaginas int not null,
    anotacoes varchar(300) not null
);

drop schema app;
drop table livro;
drop table cadastros;

select * from cadastros;

CREATE TABLE cadastros (
    nome_usuario VARCHAR(60),
    email VARCHAR(50) UNIQUE NOT NULL PRIMARY KEY,
    usuario VARCHAR(30) UNIQUE NOT NULL,
    senha VARCHAR(15) NOT NULL
);