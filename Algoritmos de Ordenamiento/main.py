def imprimir_lista(lista: list) -> None:
    """
    La función imprime una lista.
    Args: Variable lista.
    Return: None.
    """
    for i in range(len(lista)):
        print(f'[{lista[i]}]', end=' ')
    print() #salto de linea.
    
def ordenar_burbuja_list(lista: list) -> list:
    """
    La función ordena una lista.
    Args: Variable lista.
    Return: lista. ordenada.
    """
    n = len(lista) #nos devuelve el tamaño de la lista.
    for i in range(n):
        for j in range(0,n - i -1):
            if lista[j] < lista[j + 1]: #compara el valor en el indice 0 y 1
                
                #lista[j], lista[j + 1] = lista[j + 1], lista[j] Intercambia.
                #Forma Tradicional.
                aux = lista[j] 
                lista[j] = lista[j+1]
                lista[j+1] = aux

                print(f'{i},{j} se intercambiaron')
                imprimir_lista(lista)

    return lista
    

def ordenar_burbuja(matriz: list) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
        print(f'Ordenando fila {i+1}, lista actual:')
        imprimir_lista(matriz[i])
        print(matriz[i])
        matriz[i] = ordenar_burbuja_list(matriz[i])
        imprimir_lista(matriz[i])

    return matriz
    
#Lista y Matriz
lista =  [64, 34, 25, 12, 22, 11, 40, 45, 46]
matriz = [[64, 34, 25, 12, 22, 11, 40, 45, 46],
         [104, 34, 225, 12, 212, 111, 43, 40, 90],
         [645, 34, 525, 12, 722, 181, 45, 50, 5],
         [64, 34, 25, 12, 22, 11, 78, 49, 0],
         [64, 34, 25, 12, 22, 11, 80, 49, 34],
         [64, 34, 325, 12, 222, 111, 100, 3, 4],
         [64, 634, 625, 412, 22, 11, 30, 455, 1000]]

ordenar_burbuja_list(lista)
ordenar_burbuja(matriz)
