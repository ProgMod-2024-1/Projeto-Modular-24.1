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



def update_professor(updated_professor: dict) -> bool:
    data = ler_professores()
    for idx, curso in enumerate(data):
        if curso.get("codigo") == updated_professor.get("codigo"):
            data[idx] = updated_professor
            with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    return False


def atualizar_professor(matricula, professor):
    cursos = ler_professores()

    for matricula in professor:
        if professor["matricula"] == matricula:
            professor.update(professor)
            salvar_professor(cursos)
            return "sucesso"

    return "falha"


def gerar_propostas_turmas(nome, horario, matricula, disponibilidade, cursoId, creditosCurso):
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

#A partir da bela

def excluir_professor(codigo_professor):
    status, professores = ler_professores()
    if status != 3:
        return status

    if not validar_codigo(codigo_professor):
        return 5  # Falha na leitura por dados inválidos

    for i, professor in enumerate(professores):
        if professor["codigo_professor"] == codigo_professor:
            del professores[i]
            salvar_professores(professores)
            return 9  # Sucesso na exclusão

    return 10  # Falha na exclusão por inexistência

def buscar_professores_por_curso(codigo_curso):
    status, professores = ler_professores()
    if status != 3:
        return status, []

    professores_para_curso = [prof for prof in professores if any(curso['codigo'] == codigo_curso for curso in prof['cursos_ministrados'])]
    if professores_para_curso:
        return 3, professores_para_curso  # Sucesso na leitura
    return 4, []  # Falha na leitura por inexistência

def salvar_professores(professores):
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as file:
            json.dump(professores, file, ensure_ascii=False, indent=4)
        return 1  # Sucesso na atualização
    except Exception as e:
        print(f"Erro ao salvar professores: {e}")
        return 8  # Falha na atualização por dados inválidos

def validar_codigo(codigo):
    if len(codigo) != 7:
        return False
    if not codigo[:3].isalpha() or not codigo[3:].isdigit():
        return False
    return True

def validar_dados(dados):
    required_keys = ["nome", "departamento"]
    for key in required_keys:
        if key not in dados:
            return False
    return True

def atualizar_professor(codigo_professor, dados):
    status, professores = ler_professores()
    if status != 3:
        return status

    if not validar_codigo(codigo_professor):
        return 7  # Falha na atualização por inexistência

    if not validar_dados(dados):
        return 8  # Falha na atualização por dados inválidos

    for professor in professores:
        if professor["codigo_professor"] == codigo_professor:
            professor.update(dados)
            return salvar_professores(professores)

    return 7  # Falha na atualização por inexistência
