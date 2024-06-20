from flask import Blueprint, render_template, request, url_for
from project.blueprints.aluno.alunoService import *
from project.blueprints.formacao.formacaoRepo import *
from project.blueprints.filial.filialService import get_filiais
from project.blueprints.filial.filialRepo import get_all_filiais
aluno = Blueprint("aluno",__name__,url_prefix= '/aluno')

todasForms = ["ENGCMP"]
formacoes = consultaTodasFormacoes()
for formacao in formacoes:
    todasForms.append(formacao['codigo'])
    
#todasFiliais = ["A","B","C"] #consultaFiliais
dicFiliais = get_all_filiais()
todasFiliais = []
for f in dicFiliais:
    todasFiliais.append(f['nome'])

@aluno.route("/", methods=['GET', 'POST'])
def paginaAluno():
    print("Db filiais")
    print(dicFiliais)
    print(todasFiliais)
    return render_template("aluno/aluno.html")

@aluno.route("/criar", methods=['GET', 'POST'])
def paginaCriarAluno():
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
            "filiais": filiais
        }
        print(novoAluno)
        retorno = insereAluno(novoAluno)
        return render_template("aluno/exibeMsg.html",msg=retorno["mensagem"] + ".a\n Sua matricula é " + str(novoAluno["matricula"]))
    
    return render_template("aluno/formularioCria.html", filiais = todasFiliais, cursos = todasForms)

@aluno.route("/consultar", methods=['GET','POST'])
def paginaConsultarAluno():
    if request.method == 'POST':
        matricula = int(request.form["matricula"])
        retorno = buscaAluno(matricula)
        if retorno["codigo"] == 7:
            return render_template("aluno/exibeMsg.html", msg=retorno["mensagem"])
        elif retorno["codigo"] == 6:
            return render_template("aluno/respostaConsulta.html", msg=retorno["mensagem"], data = retorno["dados"])
        
    return render_template("aluno/consultaExcluiAluno.html", acao = "Consultar Aluno")

@aluno.route("/atualizar",methods=['GET','POST'])
def paginaAtualizarAluno():
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
            "filiais": filiais
        }

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
