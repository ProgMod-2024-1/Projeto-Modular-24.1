import os
import json
from project.db.database import read_db, write_db, update_db, delete_db

USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "lista_de_espera.json")

class ListaEsperaRepo:
    @staticmethod
    def lista_espera_existe(codLE):
        listas_espera = read_db(USERS_DB_URI)
        return codLE in listas_espera

    @staticmethod
    def cria_lista_espera(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
        listas_espera = read_db(USERS_DB_URI)
        if codLE not in listas_espera:
            listas_espera[codLE] = {
                'filial': filial,
                'curso': curso,
                'horario': horario,
                'matrProf': matrProf,
                'numMinimo': numMinimo,
                'tempo_desde_ultima_adicao': tempo_desde_ultima_adicao,
                'alunos': []
            }
            write_db(USERS_DB_URI, listas_espera)
            return 0  # TUDO CERTO
        return 1  # PRA Q Q VC VAI CRIAR OUTRA LISTA SE ESSA M*ERDA JA EXISTE

    @staticmethod
    def consulta_lista_espera(codLE):
        listas_espera = read_db(USERS_DB_URI)
        return listas_espera.get(codLE, {})

    @staticmethod
    def aluno_existe(matrAluno):
        return True

    @staticmethod
    def add_aluno_lista_espera(matrAluno, codLE):
        listas_espera = read_db(USERS_DB_URI)
        if codLE in listas_espera and matrAluno not in listas_espera[codLE]['alunos']:
            listas_espera[codLE]['alunos'].append(matrAluno)
            write_db(USERS_DB_URI, listas_espera)
            return 9  # O ALUNO TA DENTRO
        return 80 if matrAluno in listas_espera[codLE]['alunos'] else 71  # ALUNO E LISTA INVALIDOS

    @staticmethod
    def remove_aluno_lista_espera(matrAluno, codLE):
        listas_espera = read_db(USERS_DB_URI)
        if codLE in listas_espera and matrAluno in listas_espera[codLE]['alunos']:
            listas_espera[codLE]['alunos'].remove(matrAluno)
            write_db(USERS_DB_URI, listas_espera)
            return 9  # SE REMOVOU E PQ N PRESTA, TUDO CERTO
        return 100 if matrAluno not in listas_espera[codLE]['alunos'] else 101  # ALUNO OU LISTA ESTAO TENDO UMA CRIASE EXISTENCIAL

    @staticmethod
    def exclui_lista_espera(codLE, cria_turma):
        listas_espera = read_db(USERS_DB_URI)
        if codLE in listas_espera:
            if cria_turma:
                # QUEM TEM Q CRIAR A TURMA TA DORMINDO
                pass
            del listas_espera[codLE]
            write_db(USERS_DB_URI, listas_espera)
            return 9  # GOOOOOOOOOOOOOL
        return 10  # SE PENSO LOGO EXISTO, ESSA LISTA DE ESPERA NAO PENSA
