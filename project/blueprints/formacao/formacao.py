from flask import Blueprint, render_template, request
from formacaoService import *

formacao = Blueprint("formacao",__name__,url_prefix= '/formacao')

todosCursos = [] #consultaCursos

@formacao.route("/", methods=['GET', 'POST'])
def paginaAluno():
    return render_template("formacao/formacao.html")

@formacao.route("/criar", methods=['GET', 'POST'])
def paginaCriarForm():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        grade = request.form.getlist('grade')
        
        novaForm = {
            "codigo": codigo,
            "nome": nome,            
            "grade": grade,
            "qt_cursos": len(grade),
            "historico": []
        }
        
        retorno = insereFormacao(novaForm)
        return render_template("formacao/exibeMsg.html",msg=retorno["mensagem"])
    
    return render_template("formacao/formularioCria.html", msg=retorno["mensagem"], cursos = todosCursos, acao = "Criar Formação")

@formacao.route("/consultar", methods=['GET','POST'])
def paginaConsultarForm():
    if request.method == 'POST':
        codigo = request.form["codigo"]
        retorno = buscaFormacao(codigo)
        if retorno["codigo"] == 7:
            return render_template("formacao/exibeMsg.html", msg=retorno["mensagem"])
        elif retorno["codigo"] == 6:
            return render_template("formacao/respostaConsulta", msg=retorno["mensagem"], data = retorno["dados"], grade = retorno['dados']['grade'])
        
    return render_template("formacao/consultaExcluiForm.html", acao = "Consultar Formação")

@formacao.route("/atualizar",methods=['GET','POST'])
def paginaAtualizarForm():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        grade = request.form.getlist('grade')
        
        novosDados = {
            "codigo": codigo,
            "nome": nome,            
            "grade": grade,
            "qt_cursos": len(grade),
            "historico": []
        }

        retorno = mudaFormacao(novosDados)
        return render_template("formacao/exibeMsg.html", msg=retorno["mensagem"])
    
    return render_template("formacao/formularioCria.html", cursos = todosCursos, acao = "Atualizar Formação")

@formacao.route("excluir",methods=['GET','POST'])
def paginaExcluirForm():
    if request.method == 'POST':
        codigo = request.form["codigo"]
        dadosForm = {"codigo":codigo}
        retorno = deletaFormacao(dadosForm)
        return render_template("formacao/exibeMsg.html", msg = retorno["mensagem"])
    
    return render_template("formacao/consultaExcluiForm.html", acao = "Excluir Formação")