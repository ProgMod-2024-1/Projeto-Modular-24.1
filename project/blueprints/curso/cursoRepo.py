import os
from project.cache import cache

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'database', 'curso.json')

def salvar_curso(curso):
    try:
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r+', encoding='utf-8') as file:
                data = cache.get("curso")
                if not isinstance(data, list):
                    data = []  # Inicializa como uma lista se não for uma lista válida
                data.append(curso)

                file.seek(0)
                cache.set("curso", data)
        else:
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                cache.set("curso", [curso])
    except FileNotFoundError:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            cache.set("curso", [curso])



def ler_cursos():
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as file:
            data = cache.get("curso")
            if isinstance(data, list):
                return data
            else:
                print(f"Erro: Os dados carregados não são uma lista válida: {data}")
                return []
    except FileNotFoundError:
        return []



def get_curso(codCurs: str) -> object:
    data = ler_cursos()
    for curso in data:
        if curso.get("codigo") == codCurs:
            return curso
    return None

def update_curso(updated_curso: dict) -> bool:
    data = ler_cursos()
    for idx, curso in enumerate(data):
        if curso.get("codigo") == updated_curso.get("codigo"):
            data[idx] = updated_curso
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                cache.set("curso", data)
            return True
    return False

def salvar_cursos(cursos):
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            cache.set("curso", cursos)
    except Exception as e:
        print(f"Erro ao salvar cursos: {e}")

def validar_codigo(codigo):
    if len(codigo) != 7:
        return False
    if not codigo[:3].isalpha() or not codigo[3:].isdigit():
        return False
    return True

def validar_dados(dados):
    required_keys = ["nome", "duracao"]
    for key in required_keys:
        if key not in dados:
            return False
    return True

def atualizar_curso(codigo, dados):
    cursos = ler_cursos()
    if not validar_codigo(codigo):
        return "falha"

    if not validar_dados(dados):
        return "falha"

    for curso in cursos:
        if curso["codigo"] == codigo:
            curso.update(dados)
            salvar_cursos(cursos)
            return "sucesso"

    return "falha"

def consultar_curso(codigo):
    cursos = ler_cursos()
    if not validar_codigo(codigo):
        return "Código de curso inválido"
    for curso in cursos:
        if curso["codigo"] == codigo:
            return curso

    return "Curso não encontrado"

def excluir_curso(codigo):
    cursos = ler_cursos()
    if not validar_codigo(codigo):
        return "falha"

    for i, curso in enumerate(cursos):
        if curso["codigo"] == codigo:
            del cursos[i]
            salvar_cursos(cursos)
            return "sucesso"

    return "falha"