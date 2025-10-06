# modulo_mostrar.py
'''
NUM_MATERIAS = 5

def mostrar_uno(i, matriz, nombres, generos, legajos, estados, promedios):
    if estados[i] == 1:
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

def mostrar_todos(matriz, nombres, generos, legajos, estados, promedios):
    for i in range(len(matriz)):
        if estados[i] == 1:
            mostrar_uno(i, matriz, nombres, generos, legajos, estados, promedios)

def mostrar_ordenados(matriz, nombres, generos, legajos, estados, promedios):
    for i in range(len(matriz)):
        print("Posición", i + 1)
        print("Nombre:", nombres[i])
        print("Legajo:", legajos[i])
        print("Promedio:", round(promedios[i], 2))
        print("---------------------------")
'''
# modulo_mostrar.py

NUM_MATERIAS = 5

def mostrar_uno(i, matriz, nombres, generos, legajos, estados, promedios):
    """Muestra la información de un estudiante activo y devuelve sus datos."""
    
    estudiante_mostrado = None

    # Solo muestra si el estudiante está activo
    if estados[i] == 1:
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

        # Guardar la información mostrada
        estudiante_mostrado = {
            "nombre": nombres[i],
            "legajo": legajos[i],
            "genero": generos[i],
            "notas": matriz[i],
            "promedio": round(promedios[i], 2) if promedios[i] != 0 else None,
            "estado": "Activo"
        }
    
    return estudiante_mostrado


def mostrar_todos(matriz, nombres, generos, legajos, estados, promedios):
    """Muestra todos los estudiantes activos y devuelve su listado."""
    
    listado_estudiantes = []
    for i in range(len(matriz)):
        if estados[i] == 1:
            estudiante = mostrar_uno(i, matriz, nombres, generos, legajos, estados, promedios)
            listado_estudiantes = listado_estudiantes + [estudiante]

    return listado_estudiantes


def mostrar_ordenados(matriz, nombres, generos, legajos, estados, promedios):
    """Muestra estudiantes en orden y devuelve su información estructurada."""
    
    listado_ordenado = []
    for i in range(len(matriz)):
        print("Posición", i + 1)
        print("Nombre:", nombres[i])
        print("Legajo:", legajos[i])
        print("Promedio:", round(promedios[i], 2))
        print("---------------------------")

        estudiante = {
            "posicion": i + 1,
            "nombre": nombres[i],
            "legajo": legajos[i],
            "promedio": round(promedios[i], 2),
            "estado": "Activo" if estados[i] == 1 else "Inactivo"
        }

        listado_ordenado = listado_ordenado + [estudiante]

    return listado_ordenado
