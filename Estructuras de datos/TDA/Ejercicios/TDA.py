'''

lista_f1 = ["Audi", "BMW", "Mercedes", "Ferrarri", "Cadillac", "Alfa Romeo"]


print(lista_f1)

#Agregar elemento (al final)
lista_f1.append("Fiat")
print(lista_f1)

#Eliminar elemento
lista_f1.remove("Audi")
print(lista_f1)

lista_f1.insert(1, "Citroen")
print(lista_f1)

lista_f1.index(2, "Polo")
'''

import copy

lista_f1 = ["Audi", "Mercedes", "Ferrari", "RedBull", "Wiliams", "Alpine"]

lista_f1_copy = copy.copy(lista_f1)

#Original
print('lista original: ')
print(lista_f1)
print(id(lista_f1))

#Copia
print('lista copia: ')
print(lista_f1_copy)
print(id(lista_f1_copy))







