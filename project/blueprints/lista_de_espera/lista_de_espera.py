from flask import Blueprint,render_template,redirect, request, flash, url_for

from .listaDeEsperaService import ListaEsperaService

lista_espera_bp = Blueprint("lista_espera", __name__, url_prefix= "/lista_espera")

@lista_espera_bp.route("/")
def pagina_lista():
    print("ENTREI NA FUNCAO")    
    return render_template("lista_espera/lista_espera.html")


@lista_espera_bp.route('/lista_espera', methods=['POST'])
def cria_lista_espera():
    data = request.get_json()
    codLE = data.get('codLE')
    filial = data.get('filial')
    curso = data.get('curso')
    horario = data.get('horario')
    matrProf = data.get('matrProf')
    numMinimo = data.get('numMinimo')
    tempo_desde_ultima_adicao = data.get('tempo_desde_ultima_adicao')
    result = ListaEsperaService.cria_lista_espera(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)
    return jsonify({'result': result})

@lista_espera_bp.route('/lista_espera/<codLE>', methods=['GET'])
def consulta_lista_espera(codLE):
    result = ListaEsperaService.consulta_lista_espera(codLE)
    return jsonify(result)

@lista_espera_bp.route('/lista_espera/<codLE>/aluno', methods=['POST'])
def adiciona_aluno_lista_espera(codLE):
    data = request.get_json()
    matrAluno = data.get('matrAluno')
    result = ListaEsperaService.add_aluno_lista_espera(matrAluno, codLE)
    return jsonify({'result': result})

@lista_espera_bp.route('/lista_espera/<codLE>/aluno', methods=['DELETE'])
def remove_aluno_lista_espera(codLE):
    data = request.get_json()
    matrAluno = data.get('matrAluno')
    result = ListaEsperaService.remove_aluno_lista_espera(matrAluno, codLE)
    return jsonify({'result': result})

@lista_espera_bp.route('/lista_espera/<codLE>', methods=['DELETE'])
def exclui_lista_espera(codLE):
    cria_turma = request.args.get('cria_turma', default=False, type=bool)
    result = ListaEsperaService.exclui_lista_espera(codLE, cria_turma)
    return jsonify({'result': result})


    





