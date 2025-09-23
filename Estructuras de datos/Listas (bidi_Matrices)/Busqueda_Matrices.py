mi_matriz = [[1, 5, 3], [4, 5, 6], [7, 8, 5]]


def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"El valor {valor} se encuentra en la posición ({i}, {j})")
                #return (i, j)
    
buscar_valor_entero(mi_matriz, 5)