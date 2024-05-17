#a
def remove_elements(lista):
	lista.pop(0)
	lista.pop(3)
	lista.pop(3)
	return lista

print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


#b
def add_elements(lista):
	lista.insert(0,"Pink")
	lista.append("Yellow")
	return lista

print(add_elements(['Red', 'Green', 'White', 'Black']))


#c
def is_empty(lista):
	lista_vacia = []
	if lista == lista_vacia:
		return "Es una lista vacía"
	else:
		return "No es una lista vacía"

print(is_empty(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']))
print(is_empty([]))


#d
def check_list(lista_1, lista_2):
	if lista_1[2] == lista_2[2]:
		return True
	else:
		return False

print(check_list(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'],['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))
print(check_list(['Black', 'Pink', 'Green', 'White'],['Red', 'Green', 'Yellow', 'Black', 'Pink']))