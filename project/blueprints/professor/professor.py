from flask import Blueprint, render_template, request, redirect, url_for, flash
from .professorRepo import salvar_professor, ler_professores, atualizar_professor, excluir_professor
from .professorService import registrar_professor

professor = Blueprint('professor', __name__, url_prefix='/professor')

@professor.route('/criar', methods=['GET'])
def pagina_criar_professor():
    return render_template('professor/criar_professor.html')


@professor.route('/atualizar_professor', methods=['GET'])
def pagina_atualizar_professor():
    return render_template('professor/atualizar_professor.html')


@professor.route('/consultar', methods=['GET'])
def pagina_buscar_professor():
    return render_template('professor/consultar_professor.html')


@professor.route('/excluir', methods=['GET'])
def pagina_excluir_professor():
    return render_template('professor/excluir_professor.html')




@professor.route('/', methods=['GET'])
def listar_professores():
    professores = ler_professores()
    return render_template('professor/professor.html', professores=professores)

@professor.route('/criar', methods=['POST'])
def criar_professor():
    nome = request.form['nome']
    horario = request.form['horario']
    matricula = request.form['matricula']
    disponibilidade = request.form['disponibilidade']

    result = registrar_professor(nome, horario, matricula, disponibilidade)

    if result["success"] == 1:
        flash(result["message"], "success")
    else:
        flash(result["message"], "danger")

    return redirect(url_for('professor.listar_professores'))

@professor.route('/atualizar', methods=['POST'])
def atualizar_curso_route():
    codigoCurso = request.form['codigo']
    result = excluir_professor(codigoCurso)
    if result == "sucesso":
        nome = request.form['nome']
        horarios = request.form['horario']
        matricula = request.form['matricula']
        cursos = request.form['disponibilidade']

        novo_professor = {
            'nome': nome,
            'horarios': horarios,
            'matricula': matricula,
            'cursos': cursos,
        }

        salvar_professor(novo_professor)
        flash("Professor atualizado com sucesso!", "success")
    else:
        flash("Falha ao atualizar o professor!", "error")
    return redirect('professor.listar_professores')

#A partir da bela

@professor.route('/excluir', methods=['POST'])
def excluir_professor_route():
    codigo_professor = request.form['codigo_professor']
    status = excluir_professor(codigo_professor)
    if status == 9:
        flash("Professor excluído com sucesso!", "success")
    elif status == 10:
        flash("Falha ao excluir o professor: inexistência!", "danger")
    elif status == 5:
        flash("Falha ao excluir o professor: dados inválidos!", "danger")
    return redirect(url_for('professor.listar_professores'))

@professor.route('/consultar', methods=['POST'])
def buscar_professores_por_curso_route():
    codigo_curso = request.form['codigo_curso']
    status, resultado = buscar_professores_por_curso(codigo_curso)
    if status == 3:
        flash(f'Professores disponíveis para o curso {codigo_curso}: {len(resultado)}', "success")
    elif status == 4:
        flash("Nenhum professor disponível para o curso!", "danger")
    return redirect(url_for('professor.listar_professores'))
