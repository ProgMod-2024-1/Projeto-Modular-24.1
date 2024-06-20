import json
import os
from project.db.database import *

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'database', 'professor.json')

def salvar_professor(professor):
    try:
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    data.append(professor)
                else:
                    data = [professor]
                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump([professor], file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            json.dump([professor], file, indent=4, ensure_ascii=False)

def ler_professores():
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    print(f"Erro: Os dados carregados não são uma lista válida: {data}")
                    return []
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar JSON: {e}")
                return []
    except FileNotFoundError:
        return []



def update_professor(updated_professor: dict) -> bool:
    data = ler_professores()
    for idx, curso in enumerate(data):
        if curso.get("codigo") == updated_professor.get("codigo"):
            data[idx] = updated_professor
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    return False


def atualizar_professor(matricula, dadosProfessor):
    professores = read_db("professor")
    professor = next((professor for professor in professores if professor["matricula"] == matricula), None)
    if not professor:
        return 1
    professor.update(dadosProfessor)
    update_db(professor, 'matricula', 'professor')
    return 0


def gerar_propostas_turmas(nome, horario, matricula, disponibilidade, cursoId, creditosCurso):
    # Retorna as possiveis turmas para uma determinada matricula de um professor.
    professor = {
        "nome": nome,
        "horarios": horario,
        "matricula": matricula,
        "cursos": disponibilidade
    }

    # Verifica se a matrícula existe nos dados_professores (embora agora seja redundante)
    if professor["matricula"] != matricula:
        return {"erro": "Matrícula não encontrada"}

    # Lista de filiais
    filiais = ["Filial A", "Filial B", "Filial C"]  # Adicione ou modifique as filiais conforme necessário

    # Cria a estrutura de turmas de lista de espera
    turmas = []
    horarios_ocupados = {}  # Dicionário para controlar horários ocupados

    for curso in professor["cursos"]:
        if curso != cursoId:
            continue  # Pula os cursos que não correspondem ao cursoId fornecido

        for dia, horarios in list(professor["horarios"].items()):
            if dia not in horarios_ocupados:
                horarios_ocupados[dia] = set()

            # Determina quantos horários adicionar com base nos créditos do curso
            num_horarios = creditosCurso // 2
            horarios_turma = horarios[:num_horarios]

            # Verifica se algum dos horários já está ocupado
            horarios_disponiveis = [h for h in horarios_turma if h not in horarios_ocupados[dia]]
            if not horarios_disponiveis:
                continue  # Pula para o próximo dia se nenhum horário estiver disponível

            # Marca os horários como ocupados e remove da disponibilidade
            horarios_ocupados[dia].update(horarios_disponiveis)
            professor["horarios"][dia] = [h for h in horarios if h not in horarios_disponiveis]

            # Atribui uma filial da lista de filiais
            filial = filiais[len(turmas) % len(filiais)]

            # Cria a estrutura da turma com os horários
            horario_str = "/".join([dia + "-" + h for h in horarios_disponiveis])
            turma = {
                "MatriculaProfessor": matricula,
                "Professor": professor["nome"],
                "CursoId": cursoId,
                "Filial": filial,
                "Horario": horario_str,
                "ListaEspera": []
            }

            turmas.append(turma)

    return turmas

#A partir da bela

def excluir_professor(codigo_professor):
    status, professores = ler_professores()
    if status != 3:
        return status

    for i, professor in enumerate(professores):
        if professor["codigo_professor"] == codigo_professor:
            del professores[i]
            salvar_professor(professores)
            return 9  # Sucesso na exclusão

    return 10  # Falha na exclusão por inexistência

def buscar_professores_por_curso(codigo_curso):
    status, professores = ler_professores()
    if status != 3:
        return status, []

    professores_para_curso = [prof for prof in professores if any(curso['codigo'] == codigo_curso for curso in prof['cursos_ministrados'])]
    if professores_para_curso:
        return 3, professores_para_curso  # Sucesso na leitura
    return 4, []  # Falha na leitura por inexistência

def buscaProfessor(matricula):
    professores = read_db("professor")
    professor = next((professor for professor in professores if professor["matricula"] == matricula), None)
    if professor:
        return {
            "success": 3,
            "message": "Sucesso na consulta",
            "professor": professor
        }

    return {
        "success": 4,
        "message": "Falha professor inexistente",
        "professor": {}
    }
