from project.blueprints.filial.turmasFIlialService import *


def test_insere_turma_filial():
    ## Inserindo em Filial existente
    result = insere_turmasFilial("Teste", "2025", "EFC2435")
    assert(result,1)

    ## Inserindo em Filial nao existente
    result = insere_turmasFilial("Nao Existe", "2025", "EFC2435")
    assert(result,-1)



def remove_turmasFilial():
    ## Deletando em Filial inexistente
    result = remove_turmasFilial("Nao Existe", "2025", "EFC2435")
    assert(result,-1)

    ## Deletando de Filial Existente com ano incorreto
    result = remove_turmasFilial("Teste", "2024", "EFC2435")
    assert(result,-1)  

    ## Deletando de Filial Existente com codigo de turma incorreto
    result = remove_turmasFilial("Teste", "2024", "NaoExiste")
    assert(result,-1)      

    ## Deletando em Filial existente com codigo de turma presente
    result = remove_turmasFilial("Teste", "2025", "EFC2435")
    assert(result,1)
