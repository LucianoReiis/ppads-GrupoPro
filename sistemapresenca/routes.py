from sistemapresenca import app, database, bcrypt
from flask import render_template, redirect, flash, request
from sistemapresenca.forms import FormLogin, FormCriarConta
from sistemapresenca.models import Aluno
from flask_login import login_user, logout_user, current_user, login_required

# Criar route
# Depois função
# E template

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def loginpage():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        aluno = Aluno.query.filter_by(username=form_login.username.data).first()
        if aluno and bcrypt.check_password_hash(aluno.senha, form_login.senha.data):
            login_user(aluno, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso: {form_login.username.data}', 'alert-success') #falta implementar para aparecer no site.
            return redirect('/presenca')
        else:
            flash('Falha no Login!', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8') # criptrogafa a senha do usuário
        aluno = Aluno(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(aluno)
        database.session.commit()
        flash(f'Conta criada com sucesso: {form_criarconta.username.data}', 'alert-success') #falta implementar para aparecer no site.
        return redirect('/presenca')
    return render_template("loginpage.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route("/presenca")
@login_required
def presenca():
    return render_template("presenca.html")

@app.route("/alunos")
@login_required
def alunos():
    lista_alunos = Aluno.query.all()
    return render_template("aluno.html", lista_alunos=lista_alunos)

@app.route("/matematica")
@login_required
def matematica():
    return render_template("matematica.html")

@app.route("/portugues")
@login_required
def portugues():
    return render_template("portugues.html")

@app.route("/ciencias")
@login_required
def ciencias():
    return render_template("ciencias.html")

@app.route("/geografia")
@login_required
def geografia():
    return render_template("geografia.html")

@app.route("/historia")
@login_required
def historia():
    return render_template("historia.html")

@app.route("/artes")
@login_required
def artes():
    return render_template("artes.html")

@app.route("/educacaofisica")
@login_required
def educacaofisica():
    return render_template("educacaofisica.html")

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'logout feito com sucesso!', 'alert-success')
    return redirect('/login')


@app.route('/perfil')
@login_required
def perfil():
    return render_template("/perfil.html")
