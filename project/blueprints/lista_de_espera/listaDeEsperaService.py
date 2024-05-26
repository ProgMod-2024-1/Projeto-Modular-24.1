from .listaDeEsperaRepo import ListaEsperaRepo

class ListaEsperaService:
    
    @staticmethod
    def cria_lista_espera(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
        if not ListaEsperaRepo.lista_espera_existe(codLE):
            return ListaEsperaRepo.cria_lista_espera(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)
        return 1  # Lista já existe

    @staticmethod
    def consulta_lista_espera(codLE):
        return ListaEsperaRepo.consulta_lista_espera(codLE)

    @staticmethod
    def add_aluno_lista_espera(matrAluno, codLE):
        if ListaEsperaRepo.aluno_existe(matrAluno) and ListaEsperaRepo.lista_espera_existe(codLE):
            return ListaEsperaRepo.add_aluno_lista_espera(matrAluno, codLE)
        return 70 if not ListaEsperaRepo.aluno_existe(matrAluno) else 71

    @staticmethod
    def remove_aluno_lista_espera(matrAluno, codLE):
        if ListaEsperaRepo.aluno_existe(matrAluno) and ListaEsperaRepo.lista_espera_existe(codLE):
            return ListaEsperaRepo.remove_aluno_lista_espera(matrAluno, codLE)
        return 100 if not ListaEsperaRepo.aluno_existe(matrAluno) else 101

    @staticmethod
    def exclui_lista_espera(codLE, cria_turma):
        if ListaEsperaRepo.lista_espera_existe(codLE):
            return ListaEsperaRepo.exclui_lista_espera(codLE, cria_turma)
        return 10  # Lista inexistente
