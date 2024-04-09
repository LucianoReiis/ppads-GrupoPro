# This is a sample Python script.
from flask import Flask, render_template, request, flash, redirect
from forms import FormLogin, FormCriarConta
from fastapi import FastAPI
from routes.route import router
from routes.auth import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)
app.include_router(auth)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Altere para o URL do seu aplicativo React
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

app = Flask(__name__)

lista_alunos = ['Luciano', ' teste', 'pegar do BD']

app.config['SECRET_KEY'] = 'bfddc6059c94aa78f1f3d8be33cbdcf0894e5d8bb8960f6d3d8d3d60eecd43c9'

# Criar route
# Depois função
# E template

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def loginpage():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso: {form_login.username.data}', 'alert-success') #falta implementar para aparecer no site.
        return redirect('/presenca')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada com sucesso: {form_criarconta.username.data}', 'alert-success') #falta implementar para aparecer no site.
        return redirect('/presenca')
    return render_template("loginpage.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route("/presenca")
def presenca():
    return render_template("presenca.html")

@app.route("/alunos")
def alunos():
    return render_template("aluno.html", lista_aluno=lista_alunos)

@app.route("/matematica")
def matematica():
    return render_template("matematica.html")

@app.route("/portugues")
def portugues():
    return render_template("portugues.html")

@app.route("/ciencias")
def ciencias():
    return render_template("ciencias.html")

@app.route("/geografia")
def geografia():
    return render_template("geografia.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

@app.route("/artes")
def artes():
    return render_template("artes.html")

@app.route("/educacaofisica")
def educacaofisica():
    return render_template("educacaofisica.html")


# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
