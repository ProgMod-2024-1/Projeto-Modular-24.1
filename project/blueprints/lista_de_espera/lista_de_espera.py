from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .listaDeEsperaService import cria_lista_espera_service, consulta_lista_espera_service, add_aluno_lista_espera_service, remove_aluno_lista_espera_service, exclui_lista_espera_service

lista_espera_bp = Blueprint("lista_espera", __name__, url_prefix= "/lista_espera")

@lista_espera_bp.route("/")
def pagina_lista():
    return render_template("lista_espera/lista_espera.html")

@lista_espera_bp.route('/cria_lista_espera', methods=['POST'])
def cria_lista_espera():
    codLE = request.form['codLE']
    filial = request.form['filial']
    curso = request.form['curso']
    horario = request.form['horario']
    matrProf = request.form['matrProf']
    numMinimo = request.form['num_minimo']
    tempo_desde_ultima_adicao = request.form['tempo_desde_ultima_adicao']

    result = cria_lista_espera_service(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)

    if result == 1:
        flash('Lista de Espera criada com sucesso!')
    elif result == -1:
        flash('Erro: Chave primaria ja existe.')
    elif result == -2:
        flash('Erro nao mapeado, nao foi possivel salvar a lista de espera.')
    elif result == -3:
        flash('Erro: Objeto a ser inserido tem chaves diferentes do banco.')
    elif result == -4:
        flash('Erro: Nao foi possivel acessar o banco de dados.')
    else:
        flash('Erro desconhecido.')

    return redirect(url_for('lista_espera.pagina_lista'))

@lista_espera_bp.route('/lista_espera/<codLE>', methods=['GET'])
def consulta_lista_espera(codLE):
    result = consulta_lista_espera_service(codLE)
    return jsonify(result)

@lista_espera_bp.route('/adiciona_aluno', methods=['POST'])
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

@lista_espera_bp.route('/remove_aluno', methods=['POST'])
def remove_aluno_lista_espera():
    codLE = request.form['codLE_remove_aluno']
    matrAluno = request.form['matrAluno_remove']

    result = remove_aluno_lista_espera_service(matrAluno, codLE)

    if result == 9:
        flash('Aluno removido com sucesso!')
    else:
        flash('Erro ao remover aluno.')

    return redirect(url_for('lista_espera.pagina_lista'))

@lista_espera_bp.route('/exclui_lista_espera', methods=['POST'])
def exclui_lista_espera():
    codLE = request.form['codLE_delete']
    cria_turma = 'cria_turma' in request.form

    result = exclui_lista_espera_service(codLE, cria_turma)

    if result == 9:
        flash('Lista de Espera excluida com sucesso!')
    else:
        flash('Erro ao excluir lista de espera.')

    return redirect(url_for('lista_espera.pagina_lista'))
    
