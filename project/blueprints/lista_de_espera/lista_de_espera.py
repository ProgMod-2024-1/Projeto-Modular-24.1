from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .listaDeEsperaService import *

lista_espera = Blueprint("lista_espera", __name__, url_prefix= "/lista_espera")

@lista_espera.route("/")
def pagina_lista():
    return render_template("lista_espera/lista_espera.html")

@lista_espera.route('/cria_lista_espera', methods=['POST'])
def cria_lista_espera():
    codLE = request.form['codLE']
    nomeFili = request.form['nomeFili']
    codCurso = request.form['codCurso']
    horario = request.form['horario']
    matrProf = request.form['matrProf']
    numMinimo = request.form['num_minimo']
    tempo_desde_ultima_adicao = request.form['tempo_desde_ultima_adicao']

    result = cria_lista_espera_service(codLE, nomeFili, codCurso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)

    if result == 1:
        flash('Lista de Espera criada com sucesso!')
    elif result == -1:
        flash('Erro: Lista de Espera ja existe.')
    elif result == -2:
        flash('Erro nao mapeado, nao foi possivel salvar a lista de espera.')
    elif result == -3:
        flash('Erro: Objeto a ser inserido tem chaves diferentes do banco.')
    elif result == -4:
        flash('Erro: Nao foi possivel acessar o banco de dados.')
    else:
        flash('Erro desconhecido.')

    return redirect(url_for('lista_espera.pagina_lista'))

@lista_espera.route('/lista_espera/<codLE>', methods=['GET'])
def consulta_lista_espera(codLE):
    result = consulta_lista_espera_service(codLE)
    return jsonify(result)

@lista_espera.route('/adiciona_aluno', methods=['POST'])
def adiciona_aluno_lista_espera():
    codLE = request.form['codLE_add']
    matrAluno = request.form['matrAluno_add']

    result = add_aluno_lista_espera_service(matrAluno, codLE)

    if result == 9:
        flash('Aluno adicionado com sucesso!')
    elif result == 80:
        flash('Aluno ja esta na lista.')
    elif result == 71:
        flash('Lista de espera nao encontrada.')
    else:
        flash('Erro desconhecido ao adicionar aluno.')

    return redirect(url_for('lista_espera.pagina_lista'))

@lista_espera.route('/remove_aluno', methods=['POST'])
def remove_aluno_lista_espera():
    codLE = request.form['codLE_remove_aluno']
    matrAluno = request.form['matrAluno_remove']

    result = remove_aluno_lista_espera_service(matrAluno, codLE)

    if result == 9:
        flash('Aluno removido com sucesso!')
    elif result == 100:
        flash('Aluno inexistente.')
    elif result == 101:
        flash('Lista de espera inexistente.')
    elif result == 71:
        flash('Lista de espera nao encontrada.')
    elif result == 80:
        flash('Aluno nao encontrado na lista.')
    elif result == -1:
        flash('Erro ao remover aluno: Objeto nao encontrado.')
    elif result == -2:
        flash('Erro ao remover aluno: Erro nao mapeado.')
    elif result == -4:
        flash('Erro ao remover aluno: Banco de dados nao encontrado.')
    else:
        flash('Erro desconhecido ao remover aluno.')

    return redirect(url_for('lista_espera.pagina_lista'))

@lista_espera.route('/exclui_lista_espera', methods=['POST'])
def exclui_lista_espera():
    codLE = request.form['codLE_delete']
    cria_turma = 'cria_turma' in request.form

    result = exclui_lista_espera_service(codLE, cria_turma)

    if result == 9:
        flash('Lista de Espera excluida com sucesso!')
    elif result == 101:
        flash('Lista de espera nao encontrada.')
    elif result == -1:
        flash('Erro ao excluir lista de espera: Lista nao encontrada.')
    elif result == -4:
        flash('Erro ao excluir lista de espera: Banco de dados nao encontrado.')
    else:
        flash('Erro desconhecido ao excluir lista de espera.')

    return redirect(url_for('lista_espera.pagina_lista'))

    