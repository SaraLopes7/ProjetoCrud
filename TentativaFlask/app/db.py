import mysql.connector

#essas configurações deve ser mudada quando for configurar o servidor para deploy
db = mysql.connector.connect( host="localhost",
                              user="root",
                              password="lopesSara7#",
                              database="db_livraria"
)

mycursor = db.cursor()