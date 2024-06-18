from .professorRepo import salvar_professor, ler_professores

def registrar_professor(nome: str, horario: str, matricula: str, disponibilidade: str) -> dict:
    professor = {
        'nome': nome,
        'horario': horario,
        'matricula': matricula,
        'disponibilidade': disponibilidade
    }
    salvar_professor(professor)
    return {
        "success": 1,
        "message": "Professor registrado com sucesso",
        "professor": professor
    }

def listar_professores() -> list:
    return ler_professores()
