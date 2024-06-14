from project.db import database
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .alunoRepo import salvar_aluno, criar_aluno
aluno = Blueprint('aluno', __name__, url_prefix='/aluno')

@aluno.route('/criar', methods=['GET'])
def pagina_criar_aluno():
    return render_template('aluno/criar_aluno.html')


@aluno.route('/criar', methods=['POST'])
def criar_dados_aluno():
    nome = request.form['nome']
    endereco = request.form['endereco']
    status = request.form['status']
    preferencias_filiais = request.form['preferencias_filiais']
    cursos_e_formacoes_feitas = request.form['cursos_e_formacoes_feitas']
    cursos_avulsos= request.form['cursos_avulsos']
    formacoes_atuais = request.form['formacoes_atuais']
    lista_espera = request.form['lista_espera']
    
    
    aluno_novo = {
    "matricula": "",
    "nome": nome,
    "endereco": endereco,
    "status": status,
    "preferencia_filiais": preferencias_filiais,
    "cursos_e_formacoes_feitas":cursos_e_formacoes_feitas,
    "cursos_avulsos": cursos_avulsos,
    "formacoes_atuais": formacoes_atuais,
    "listas_espera": lista_espera
}
    criar_aluno(aluno_novo)
    
    return redirect(url_for('aluno.pagina_criar_aluno'))