# modulo_mostrar.py

NUM_MATERIAS = 5

def mostrar_uno(i, matriz, nombres, generos, legajos, promedios):
    
    print("---------------------------")
    print("Nombre:", nombres[i])
    print("Legajo:", legajos[i])
    print("Género:", generos[i])
    print("Notas:")
    for j in range(NUM_MATERIAS):
        print("  MATERIA_" + str(j + 1) + ":", matriz[i][j])
    if promedios[i] != 0:
        print("Promedio:", round(promedios[i], 2))
    print("---------------------------")

def mostrar_todos(matriz, nombres, generos, legajos, promedios):
    
    for i in range(len(matriz)):
        mostrar_uno(i, matriz, nombres, generos, legajos, promedios)

def mostrar_ordenados(matriz, nombres, generos, legajos, promedios):

    for i in range(len(matriz)):
        print("Posición", i + 1)
        print("Nombre:", nombres[i])
        print("Legajo:", legajos[i])
        print("Promedio:", round(promedios[i], 2))
        print("---------------------------")
