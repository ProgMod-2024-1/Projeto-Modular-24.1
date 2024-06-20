from flask import Blueprint,render_template,redirect, request, flash, url_for, jsonify
from project.blueprints.certificacao.certificacaoService import seek_certificacoes_aluno, get_certificacoes, seek_certificacoes, muda_certificacoes
from flask_login import current_user
from project.utils import aluno_required

certificacao = Blueprint("certificacao",__name__,url_prefix= '/certificacao')

#Página que mostra todas as certificações de um aluno
@certificacao.route("/")
#@aluno_required
def mostra_certificacoes_route():
    certificacoes = seek_certificacoes_aluno(current_user.id)
    return render_template("certificacao/mostra-certificacoes.html", current_user=current_user, certificacoes = certificacoes)

#Página onde é possível ver todas as informações sobre uma certificação específica
@certificacao.route("/ver_certificacoes")
#@aluno_required
def ver_info_certificacoes_route():

    codAluno = request.args.get('codAluno')
    formacao = request.args.get('formacao')

    data = seek_certificacoes(codAluno, formacao)

    return render_template("certificacao/ver-certificacao.html", codAluno=codAluno, certificacao = data)




