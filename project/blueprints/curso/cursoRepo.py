import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'database', 'curso.json')

def salvar_curso(curso):
    try:
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []  # Inicializa como uma lista se não for uma lista válida
                except json.JSONDecodeError:
                    data = []  # Em caso de erro de decodificação

                data.append(curso)

                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump([curso], file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            json.dump([curso], file, indent=4, ensure_ascii=False)



def ler_cursos():
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
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    return False
