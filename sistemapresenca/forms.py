from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, equal_to, ValidationError
from sistemapresenca.models import Aluno


# Formularios de Cadastro e Logins
class FormCriarConta(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(5, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit_criarconta = SubmitField('Criar conta')


    def validate_email(self, email):
        aluno = Aluno.query.filter_by(email=email.data).first()
        if aluno:
            raise ValidationError('E-mail já cadastrado')

    def validate_username(self, username):
        aluno = Aluno.query.filter_by(username=username.data).first()
        if aluno:
            raise ValidationError('Username já cadastrado')




class FormLogin(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(),])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(5, 20)])
    lembrar_dados = BooleanField('Lembrar senha')
    botao_submit_login = SubmitField('Fazer Login')

