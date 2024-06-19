from filialRepo import get_filial_by_codigo, update_filial, get_all_filiais

def insere_turmasFilial(filial_nome: str, ano: str, turma_codigo: str)->int:
	query = get_all_filiais()
	query_element = []
	for filial in query:
		query_elements.append(list(filial["turmas"].values()))

	for filial in query_element:
		for elements in filial:
			for codigos in elements:
				if codigos == turma_codigo:
					return -1

	filial = get_filial(filial_nome)

	# Ele verifica se há a key ano no dic, caso n tenha ele criara com []
	# como elemento
	filial["turmas"].setdefault(ano, [])

	# Atualiza a lista dos elementos da key ano
	lista_aux = filial["turmas"].get(ano)
	lista_aux[0].append(turma_codigo)

	# Da um update nos elementos da key ano
	filial["turmas"].update(ano, lista_aux[0])

	# Da um update do objeto filial
	update_filial(filial)




def remove_turmasFilial(filial_nome: str, ano: str, turma_codigo: str)->int:
	query = get_all_filiais()
	query_element = []
	for filial in query:
		query_elements.append(list(filial["turmas"].values()))

	for filial in query_element:
		for elements in filial:
			for codigos in elements:
				if codigos == turma_codigo:
					flag = 1

	if(!flag):
		return -1

	filial = get_filial(filial_codigo)

	# Atualiza a lista dos elementos da key ano
	lista_aux = filial["turmas"].get(ano)
	lista_aux[0].remove(turma_codigo)

	# Da um update nos elementos da key ano
	filial["turmas"].update(ano, lista_aux[0])

	# Da um update do objeto filial
	update_filial(filial)