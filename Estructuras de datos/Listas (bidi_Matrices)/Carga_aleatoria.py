matriz = [[0]*10 for _ in range(10)]

def cargar_matriz_secuencial(matriz: list):
    seguir = "S"
    while seguir == "S":
        fila = int(input("Ingrese la fila donde quiere cargar el dato (0-9): "))
        columna = int(input("Ingrese la columna donde quiere cargar el dato (0-9): "))
        dato = int(input("Ingrese el dato que quiere cargar: "))
        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando datos? S/N: ")

cargar_matriz_secuencial(matriz)
print(matriz)
