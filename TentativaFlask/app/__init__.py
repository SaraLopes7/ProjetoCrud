from flask import Flask
from flask_mysqldb import MySQLdb

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = 'CHAVE'

db = MySQLdb(app)