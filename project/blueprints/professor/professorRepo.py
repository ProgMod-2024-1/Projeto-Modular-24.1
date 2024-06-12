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
