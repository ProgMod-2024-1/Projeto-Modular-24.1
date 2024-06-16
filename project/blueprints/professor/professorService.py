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


def gerar_turmas_lista_espera(matricula: str, dados_professores: list, cursoId: str, creditosCurso: int):
    # Verifica se a matrícula existe nos dados_professores
    professor = next((prof for prof in dados_professores if prof["matricula"] == matricula), None)
    if not professor:
        return {"erro": "Matrícula não encontrada"}
    
    # Lista de filiais
    filiais = ["Filial A", "Filial B", "Filial C"]  # Adicione ou modifique as filiais conforme necessário
    
    # Cria a estrutura de turmas de lista de espera
    turmas = []
    horarios_ocupados = {}  # Dicionário para controlar horários ocupados
    
    for curso in professor["cursos"]:
        if curso != cursoId:
            continue  # Pula os cursos que não correspondem ao cursoId fornecido

        for dia, horarios in list(professor["horarios"].items()):
            if dia not in horarios_ocupados:
                horarios_ocupados[dia] = set()
            
            # Determina quantos horários adicionar com base nos créditos do curso
            num_horarios = creditosCurso // 2
            horarios_turma = horarios[:num_horarios]
            
            # Verifica se algum dos horários já está ocupado
            horarios_disponiveis = [h for h in horarios_turma if h not in horarios_ocupados[dia]]
            if not horarios_disponiveis:
                continue  # Pula para o próximo dia se nenhum horário estiver disponível
            
            # Marca os horários como ocupados e remove da disponibilidade
            horarios_ocupados[dia].update(horarios_disponiveis)
            professor["horarios"][dia] = [h for h in horarios if h not in horarios_disponiveis]
            
            # Atribui uma filial da lista de filiais
            filial = filiais[len(turmas) % len(filiais)]
            
            # Cria a estrutura da turma com os horários
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