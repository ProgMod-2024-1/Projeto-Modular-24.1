from flask import Blueprint, render_template, request, redirect, url_for, flash
from .professorRepo import salvar_professor, ler_professores, atualizar_professor
from .professorService import registrar_professor

professor = Blueprint('professor', __name__, url_prefix='/professor')

@professor.route('/criar', methods=['GET'])
def pagina_criar_professor():
    return render_template('professor/criar_professor.html')




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
def atualizar_professor():
    matriculaProfessor = request.form['matricula']
    result = excluir_professor(matriculaProfessor)

    if result == "sucesso":
      nome = request.form['nome']
      horario = request.form['horario']
      matricula = request.form['matricula']
      disponibilidade = request.form['disponibilidade']
      cursos = request.form['cursos']

      novo_professor = {
          "nome": nome,
          "horarios": horario,
          "matricula": "12345",
          "cursos": cursos
      }

      salvar_professor(novo_professor)
      flash(result["Professor atualizado com sucesso"], "success")
    
    else:
        flash(result["Erro ao atualizar professor"], "error")

    return redirect(url_for('/principal'))

