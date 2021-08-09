from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9ae0fc9ba4ef967c995959a2f18485f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  #sqlalchemy instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.load_view = 'login'

from Event import routes