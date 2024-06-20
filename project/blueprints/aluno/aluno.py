from flask import Blueprint, render_template, request, url_for
from project.blueprints.aluno.alunoService import *
from project.blueprints.formacao.formacaoRepo import *
from project.blueprints.filial.filialService import get_filiais
from project.blueprints.filial.filialRepo import get_all_filiais
from flask_login import current_user
aluno = Blueprint("aluno",__name__,url_prefix= '/aluno')

    
@aluno.route("/", methods=['GET', 'POST'])
def paginaAluno():
    return render_template("aluno/aluno.html")

@aluno.route("/criar", methods=['GET', 'POST'])
def paginaCriarAluno():
    print(current_user.id)
    dicFiliais = get_all_filiais()
    print(dicFiliais)
    todasFiliais = []
    for f in dicFiliais:
        todasFiliais.append(f['nome'])

    todasForms = []
    formacoes = consultaTodasFormacoes()
    for formacao in formacoes:
        todasForms.append(formacao['codigo'])

    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        cep = request.form['cep']
        formacao = request.form['formacao']
        filiais = request.form.getlist('filiais')
        
        novoAluno = {
            "matricula": geraNovaMatricula(),
            "nome": nome,
            "endereco": endereco,
            "cep": cep,
            "cpf": cpf,
            "formacao": formacao,
            "filiais": filiais,
            "cursos": [],
            "avaliacao": [],
            "user": current_user.id
        }
        print(novoAluno)
        retorno = insereAluno(novoAluno)
        return render_template("aluno/exibeMsg.html",msg=retorno["mensagem"] + ". Sua matricula é " + str(novoAluno["matricula"]))
    
    return render_template("aluno/formularioCria.html", filiais = todasFiliais, cursos = todasForms)

@aluno.route("/consultar", methods=['GET','POST'])
def paginaConsultarAluno():
    if request.method == 'POST':
        matricula = int(request.form["matricula"])
        retorno = buscaAluno(matricula)
        if retorno["codigo"] == 7:
            return render_template("aluno/exibeMsg.html", msg=retorno["mensagem"])
        elif retorno["codigo"] == 6:
            dadosAluno = retorno["dados"]
            print(dadosAluno)
            if "cursos" in dadosAluno:
                listaCursos = []
                for curso in dadosAluno["cursos"]:
                    listaCursos.append(curso["curso"])
                return render_template("aluno/respostaConsulta.html", msg=retorno["mensagem"], data = dadosAluno, filiais = dadosAluno["filiais"], cursos = listaCursos)
            else:
                return render_template("aluno/respostaConsulta.html", msg=retorno["mensagem"], data = dadosAluno, filiais = dadosAluno["filiais"], cursos = [])

    return render_template("aluno/consultaExcluiAluno.html", acao = "Consultar Aluno")

@aluno.route("/atualizar",methods=['GET','POST'])
def paginaAtualizarAluno():
    dicFiliais = get_all_filiais()
    print(dicFiliais)
    todasFiliais = []
    for f in dicFiliais:
        todasFiliais.append(f['nome'])

    todasForms = ["ENGCMP"]
    formacoes = consultaTodasFormacoes()
    for formacao in formacoes:
        todasForms.append(formacao['codigo'])
        
    if request.method == 'POST':
        matricula = request.form["matricula"] 
        nome = request.form['nome']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        cep = request.form['cep']
        formacao = request.form['formacao']
        filiais = request.form.getlist('filiais')

        novosDados = {
            "matricula":int(matricula),
            "nome": nome,
            "endereco": endereco,
            "cep": cep,
            "cpf": cpf,
            "formacao": formacao,
            "filiais": filiais,
            "cursos": [],
            "avaliacao": [],
            "user": ""
        }

        dadosAluno = consultaAluno(int(matricula))
        if dadosAluno != None:
            novosDados["cursos"] = dadosAluno["cursos"]
            novosDados["user"] = dadosAluno["user"]
            novosDados["avaliacao"] = dadosAluno["avaliacao"]
        retorno = mudaAluno(novosDados)
        return render_template("aluno/exibeMsg.html", msg=retorno["mensagem"])
    
    return render_template("aluno/formularioAtualiza.html", filiais = todasFiliais, cursos = todasForms)

@aluno.route("excluir",methods=['GET','POST'])
def paginaExcluirAluno():
    if request.method == 'POST':
        matricula = request.form["matricula"]
        dadosAluno = {"matricula":int(matricula)}
        retorno = deletaAluno(dadosAluno)
        return render_template("aluno/exibeMsg.html", msg = retorno["mensagem"])
    
    return render_template("aluno/consultaExcluiAluno.html", acao = "Excluir Aluno")
