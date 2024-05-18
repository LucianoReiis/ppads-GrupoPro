from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bfddc6059c94aa78f1f3d8be33cbdcf0894e5d8bb8960f6d3d8d3d60eecd43c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nmeCPCqQYNonRjsfoFFJVuGlMPLUYLTp@monorail.proxy.rlwy.net:49830/railway'

#if os.getenv("DATABASE_URL"):
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") # Banco de dados Railway (online)
#else:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodedados.db' # Banco de dados local

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginpage'
login_manager.login_message_category = 'alert-info'

from sistemapresenca import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("alunos"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("banco de dados criado com sucesso")
else:
    print("base de dados já existente")


from sistemapresenca import routes

