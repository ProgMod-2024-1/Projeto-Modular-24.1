from cursoRepo import get_curso, update_curso

def defPreReq(db_path, codCurs, codPreReq):
    curso = get_curso(db_path, codCurs)
    if curso:
        if codPreReq not in curso['preRequisitos']:
            curso['preRequisitos'].append(codPreReq)
            return update_curso(db_path, curso)
    return False

def defProfDispCurs(db_path, codCurs, matrProf):
    curso = get_curso(db_path, codCurs)
    if curso:
        if matrProf not in curso['professoresDisponiveis']:
            curso['professoresDisponiveis'].append(matrProf)
            return update_curso(db_path, curso)
    return False
