import mysql.connector

#essas configurações devem ser mudadas quando for configurar o servidor para deploy
db = mysql.connector.connect( host="localhost",
                              user="root",
                              password="teste",
                              database="db_livraria"
)

mycursor = db.cursor()