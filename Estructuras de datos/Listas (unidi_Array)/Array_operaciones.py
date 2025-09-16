mi_lista_1 = ["C", "C++", "Java", "Python", "JavaScript"]
mi_lista_2 = ["HTML", "CSS", "SQL", "NoSQL"]
mi_lista_3 = ["d", "a", "c", "b", "e"]
mi_lista_4 = [3, 1, 4, 2, 5]


# Funcion Append: Agrega un elemento al final de la lista, a menos que se especifique un índice
mi_lista_1.append("PHP")
print(mi_lista_1)

# Funcion Pop: Elimina el último elemento de la lista, a menos que se especifique un índice
mi_lista_1.pop(0)
print(mi_lista_1)


# Funcion sort: Ordena los elementos de la lista en orden ascendente

mi_lista_3.sort()
print(mi_lista_3)

# Funcion reverse: Invierte el orden de los elementos en la lista
mi_lista_4.reverse()
print(mi_lista_4)


# Funcion extend: Agrega los elementos de una lista al final de otra lista
mi_lista_1.extend(mi_lista_2)
print(mi_lista_1)

# Funcion insert: Inserta un elemento en una posición específica de la lista
mi_lista_1.insert(0, "TypeScript")
print(mi_lista_1)