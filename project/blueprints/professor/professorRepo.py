import json
import os

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

def get_professor(matricula: str) -> object:
    data = ler_professores()
    for professor in data:
        if professor.get("matricula") == matricula:
            return professor
    return None

def update_professor(updated_professor: dict) -> bool:
    data = ler_professores()
    for idx, professor in enumerate(data):
        if professor.get("matricula") == updated_professor.get("matricula"):
            data[idx] = updated_professor
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    return False

def atualizar_professor(matricula, dados_atualizados):
    professores = ler_professores()
    for idx, professor in enumerate(professores):
        if professor["matricula"] == matricula:
            professores[idx].update(dados_atualizados)
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump(professores, file, indent=4, ensure_ascii=False)
            return "sucesso"
    return "falha"

def salvar_professores(professores):
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            json.dump(professores, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar professor: {e}")

def validar_codigo(codigo):
    if len(codigo) != 7:
        return False
    if codigo.isnumeric():
        return True
    return False

def validar_dados(dados):
    required_keys = ["nome", "duracao"]
    for key in required_keys:
        if key not in dados:
            return False
    return True

def gerar_propostas_turmas(nome, horario, matricula, disponibilidade, cursoId, creditosCurso):
    professor = {
        "nome": nome,
        "horarios": horario,
        "matricula": matricula,
        "cursos": disponibilidade
    }

    if professor["matricula"] != matricula:
        return {"erro": "Matrícula não encontrada"}

    filiais = ["Filial A", "Filial B", "Filial C"]

    turmas = []
    horarios_ocupados = {}

    for curso in professor["cursos"]:
        if curso != cursoId:
            continue

        for dia, horarios in list(professor["horarios"].items()):
            if dia not in horarios_ocupados:
                horarios_ocupados[dia] = set()

            num_horarios = creditosCurso // 2
            horarios_turma = horarios[:num_horarios]

            horarios_disponiveis = [h for h in horarios_turma if h not in horarios_ocupados[dia]]
            if not horarios_disponiveis:
                continue

            horarios_ocupados[dia].update(horarios_disponiveis)
            professor["horarios"][dia] = [h for h in horarios if h not in horarios_disponiveis]

            filial = filiais[len(turmas) % len(filiais)]

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

def consultar_professor(codigo):
    professores = ler_professores()
    if not validar_codigo(codigo):
        return "Código de curso inválido"
    for professor in professores:
        if professor["matricula"] == codigo:
            return professor

    return "Professor não encontrado"

def excluir_professor(matricula):
    professores = ler_professores()
    if not validar_codigo(matricula):
        return "falha"

    for i, professor in enumerate(professores):
        if professor["matricula"] == matricula:
            del professores[i]
            salvar_professores(professores)
            return "sucesso"

    return "falha"
