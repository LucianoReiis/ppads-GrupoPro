from sistemapresenca import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_aluno(id_aluno):
    return Aluno.query.get(int(id_aluno))



# Tabelas do Banco de Dados
class Aluno(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    #curso = database.relationship('materia', backref='materia', lazy=True)



class Cursos(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    materia = database.Column(database.String, nullable=False, unique=True)
    aulas = database.Column(database.String, nullable=False)
    id_aluno = database.Column(database.Integer, database.ForeignKey('aluno.id'), nullable=False)
