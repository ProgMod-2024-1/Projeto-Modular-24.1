import json
import os

# Caminho para o arquivo JSON na pasta database
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'database', 'curso.json')

def salvar_curso(curso):
    try:
        with open(CAMINHO_ARQUIVO, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(curso)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            json.dump([curso], file, indent=4, ensure_ascii=False)

def ler_cursos():
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
