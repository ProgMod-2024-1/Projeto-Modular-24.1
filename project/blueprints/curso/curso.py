from flask import Blueprint, render_template, request, redirect, url_for
from .cursoRepo import salvar_curso, ler_cursos

curso = Blueprint('curso', __name__, url_prefix='/curso')

@curso.route('/criar', methods=['GET'])
def pagina_criar_curso():
    return render_template('cursos/criar_curso.html')

# Rota para listar os cursos
@curso.route('/', methods=['GET'])
def listar_cursos():
    # Aqui você pode implementar a lógica para buscar os cursos do banco de dados
    # ou de onde você os armazena. Por enquanto, vamos apenas renderizar um template vazio.
    cursos = []  # Você deve preencher essa lista com os cursos reais
    return render_template('cursos/curso.html', cursos=cursos)

@curso.route('/criar', methods=['POST'])
def criar_curso():
    nome = request.form['nome']
    descricao = request.form['descricao']
    codigo = request.form['codigo']
    pre_requisitos = request.form['pre_requisitos']
    creditos = request.form['creditos']
    criterios_aprovacao = request.form['criterios_aprovacao']

    novo_curso = {
        'nome': nome,
        'descricao': descricao,
        'codigo': codigo,
        'pre_requisitos': pre_requisitos,
        'creditos': creditos,
        'criterios_aprovacao': criterios_aprovacao
    }

    salvar_curso(novo_curso)
    return redirect(url_for('curso.pagina_criar_curso'))

