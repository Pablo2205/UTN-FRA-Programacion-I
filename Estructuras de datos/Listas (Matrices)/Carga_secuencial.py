def cargar_matriz_secuencial(matriz: list) -> list:
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[filas])):
            matriz[filas][columnas] = int(input(f'Ingrese el elemento fila {filas+1} columna {columnas+1}: '))
    return matriz

mi_matriz = matriz
cargar_matriz_secuencial(mi_matriz)
