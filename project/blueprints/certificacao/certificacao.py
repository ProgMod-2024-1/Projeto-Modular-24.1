from flask import Blueprint,render_template,redirect, request, flash, url_for, jsonify
from project.blueprints.certificacao.certificacaoService import get_certificacoes, registra_certificacoes, seek_certificacoes, muda_certificacoes
from flask_login import current_user

certificacao = Blueprint("certificacao",__name__,url_prefix= '/certificacao')

#Página que mostra todas as certificações de um aluno
@certificacao.route("/")
def mostra_certificacoes_route():
    certificacoes = get_certificacoes()
    return render_template("certificacao/mostra-certificacoes.html", current_user=current_user, certificacoes = certificacoes)

#Página onde é possível ver todas as informações sobre uma certificação específica
@certificacao.route("/ver_certificacoes")
def ver_info_certificacoes_route():

    codCert = request.args.get('codCert')
    codAluno = request.args.get('id_aluno')
    id_formacao = request.args.get('id_formacao')

    data = seek_certificacoes(codAluno)

    return render_template("certificacao/ver-certificacao.html", certificacao = data)




