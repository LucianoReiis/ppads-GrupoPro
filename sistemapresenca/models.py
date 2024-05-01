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

class Alunos(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    matricula = database.Column(database.Integer, nullable=False)
    nome = database.Column(database.String, nullable=False)
    materia = database.Column(database.String, nullable=False)
    turma = database.Column(database.String, nullable=False, default="1A")
    aulas = database.Column(database.String, nullable=False)





