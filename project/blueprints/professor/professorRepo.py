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


def gerar_turmas_lista_espera(nome, horario, matricula, disponibilidade, cursoId, creditosCurso):
    # Retorna as possiveis turmas para uma determinada matricula de um professor.
    professor = {
        "nome": nome,
        "horarios": horario,
        "matricula": matricula,
        "cursos": disponibilidade
    }
    
    # Verifica se a matrícula existe nos dados_professores (embora agora seja redundante)
    if professor["matricula"] != matricula:
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