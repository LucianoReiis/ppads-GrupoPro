from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bfddc6059c94aa78f1f3d8be33cbdcf0894e5d8bb8960f6d3d8d3d60eecd43c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodedados.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginpage'
login_manager.login_message_category = 'alert-info'

from sistemapresenca import routes
