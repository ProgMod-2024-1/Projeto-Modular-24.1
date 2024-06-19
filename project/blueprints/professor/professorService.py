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

#A partir da bela

def buscar_professores_por_curso(codigo_curso: str) -> dict:
    status, professores_disponiveis = buscar_professores_por_curso(codigo_curso)
    return {
        "success": status,
        "message": "Professores encontrados" if status == 3 else "Nenhum professor disponível para o curso",
        "professores": professores_disponiveis
    }

def excluir_professor_service(codigo_professor: str) -> dict:
    status = excluir_professor(codigo_professor)
    return {
        "success": 1 if status == 9 else 0,
        "message": "Professor excluído com sucesso" if status == 9 else "Falha ao excluir o professor"
    }
