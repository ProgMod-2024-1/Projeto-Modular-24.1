import json

def load_data(db_path):
    with open(db_path, 'r') as file:
        return json.load(file)

def save_data(db_path, data):
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_curso(db_path, codCurs):
    data = load_data(db_path)
    for curso in data['cursos']:
        if curso['id'] == codCurs:
            return curso
    return None

def update_curso(db_path, curso):
    data = load_data(db_path)
    for idx, existing_curso in enumerate(data['cursos']):
        if existing_curso['id'] == curso['id']:
            data['cursos'][idx] = curso
            save_data(db_path, data)
            return True
    return False
