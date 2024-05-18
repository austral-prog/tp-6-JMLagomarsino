# Replace the "ANSWER HERE" with your answer

def remove_elements(lista):
	lista.pop(0)
	lista.pop(3)
	if len(lista) > 2:
		lista.pop(3)
	
	return lista

def add_elements(lista):
	lista.insert(0,"Pink")
	lista.append("Yellow")
	return lista

def is_empty(lista):
	lista_vacia = []
	if lista == lista_vacia:
		return True
	else:
		return False


def check_lists(lista_1, lista_2):
	if lista_1[2] == lista_2[2]:
		return True
	else:
		return False


def list_of_lists(lista):
	result = []
	if len(lista[0]) >= 2:
		result.append(lista[0][:2])
	else:
		result.append(lista[0])
	if len(lista[1]) >= 4:
		result.append(lista[1][1:4])
	elif len(lista[1]) > 1:
		result.append(lista[1][1:])
	else:
		result.append([])
	if len(lista[2]) >= 2:
		result.append(lista[2][-2:])
	else:
		result.append(lista[2])
	return result
