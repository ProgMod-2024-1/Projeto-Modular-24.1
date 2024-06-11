from cursoRepo import get_curso, update_curso

def register_pre_requisito(codCurs: str, codPreReq: str) -> object:
    curso = get_curso(codCurs)
    if curso:
        if codPreReq not in curso["preRequisitos"]:
            curso["preRequisitos"].append(codPreReq)
            if update_curso(curso):
                return {
                    "success": 1,
                    "message": "Pré-requisito adicionado com sucesso",
                    "curso": curso
                }
    return {
        "success": 0,
        "message": "Falha ao adicionar pré-requisito ou pré-requisito já existente",
        "curso": None
    }

def register_professor_disponivel(codCurs: str, matrProf: str) -> object:
    curso = get_curso(codCurs)
    if curso:
        if matrProf not in curso["professoresDisponiveis"]:
            curso["professoresDisponiveis"].append(matrProf)
            if update_curso(curso):
                return {
                    "success": 1,
                    "message": "Professor disponível adicionado com sucesso",
                    "curso": curso
                }
    return {
        "success": 0,
        "message": "Falha ao adicionar professor disponível ou professor já existente",
        "curso": None
    }
