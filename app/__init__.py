from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = 'CHAVE'

login_manager = LoginManager(app)