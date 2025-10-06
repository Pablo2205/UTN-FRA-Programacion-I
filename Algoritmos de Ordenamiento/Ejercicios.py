#Ejercicio 2 ordenamieto: https://docs.google.com/document/d/1c78QvjZf2nQmf3VpBNlytkrqZ9aE3gIXqV5l_bs7yFY/edit?tab=t.0

# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.


def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end= " ")



def intercalar_vectores(lista_uno: list, lista_dos: list, orden_descendente: bool = False) -> list:
    """
    Recibe dos vectores de números enteros, los unifica y ordena.

    Args:
        lista_uno (list): Primer lista de números enteros a ordenar.
        lista_dos (list): Segunda lista de números enteros a ordenar.
        orden_descendente (bool, optional): Si es True, ordena las listas de forma descendente. Default es False.

    Returns:
        list: Un array unificando y ordenando las listas.
    """
    
    lista_unificada = lista_uno + lista_dos
    
    for i in range(len(lista_unificada)):
        for j in range(len(lista_unificada)):
            if orden_descendente == False:
                if  lista_unificada[i] < lista_unificada[j]:
                    lista_unificada[i], lista_unificada[j] = lista_unificada[j], lista_unificada[i]
            else:
                if  lista_unificada[i] > lista_unificada[j]:
                    lista_unificada[i], lista_unificada[j] = lista_unificada[j], lista_unificada[i]

    return lista_unificada



lista_test = [4, 1, 3, 5, 2]
lista_test_dos = [6, 10, 9, 7, 8]

mostrar_lista(lista_test)
print()
mostrar_lista(lista_test_dos)
print()
print()

lista_ordenada = intercalar_vectores(lista_test, lista_test_dos) #Acá se puede poner como terceer valor "True" para que se ordene de forma descendente. 

mostrar_lista(lista_ordenada)
