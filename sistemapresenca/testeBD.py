from sistemapresenca import app, database
from sistemapresenca.models import Aluno, Alunos
from sqlalchemy import text


with app.app_context():
    # database.drop_all()# Deleta o Banco de dados
    database.create_all() # Cria o Banco de dados

    # matriculas = ["1235"]
    # lista_alunos = ["Rodolfo"]
    # materia = ["Matemática", "Português", "Ciências", "Geografia", "História", "Artes", "Educação_Física"]
    # aulas = ["Aluna 1", "Aluna 2", "Aluna 3", "Aluna 4", "Aluna 5", "Aluna 6", "Aluna 7"]
    #
    # for x, aluno in enumerate(lista_alunos):
    #     for materia in materia:
    #         for aula in aulas:
    #             insert_query = text(
    #                 f"INSERT INTO Alunos (matricula, nome, materia, turma, aulas) VALUES ('{matriculas[x]}', '{aluno}', '{materia}', '1A', '{aula}')")
    #             database.session.execute(insert_query)
    #
    # # Commit as alterações no banco de dados
    # database.session.commit()



    # lista_alunos = database.session.query(Alunos).all()
    #
    # alunos_agrupados = []
    #
    # for aluno in lista_alunos:
    #     if aluno.matricula not in alunos_agrupados:
    #         alunos_agrupados.append(aluno.matricula)
    #
    # for matricula in alunos_agrupados:
    #     query_materias = database.session.query(Alunos).filter_by(matricula=matricula).all()
    #     aluno = database.session.query(Alunos.nome).filter_by(matricula=matricula).first()
    #     turma = database.session.query(Alunos.turma).filter_by(matricula=matricula).first()
    #
    #     print(aluno)
    #     print(turma)
    #
    #     for materia_por_aluno in query_materias:
    #         print(f"Materia: {materia_por_aluno.materia}")
    #     print()
    #


    # lista_alunos = database.session.query(Alunos).all()
    # materias_por_matricula = {}
    #
    # for aluno in lista_alunos:
    #     if aluno.matricula not in materias_por_matricula:
    #         materias_por_matricula[aluno.matricula] = []
    #     materias_por_matricula[aluno.matricula].append(aluno.materia)
    #
    # print(materias_por_matricula)
    #
    # # Agora, imprima todas as matérias para cada matrícula
    # for matricula, materias in materias_por_matricula.items():
    #     aluno = database.session.query(Alunos.nome).filter_by(matricula=matricula).first()
    #     print(aluno.nome)
    #     print(f"Matrícula: {matricula}")
    #     for materia in materias:
    #         print(f"Matéria: {materia}")
    #     print()  # Linha em branco para separar os grupos

