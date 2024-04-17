from sistemapresenca import app, database
from sistemapresenca.models import Aluno

with app.app_context():
    #database.drop_all()# Deleta o Banco de dados
    database.create_all() # Cria o Banco de dados


    #print(Aluno.query.all())
    #aluno = Aluno.query.first()
    #print(aluno.email)