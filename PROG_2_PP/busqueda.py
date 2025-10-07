
def buscar_por_legajo(legajo, legajos):
    """Busca la posición de un estudiante según su legajo.

    Args:
        legajo (int): Legajo a buscar.
        legajos (list[int]): Lista de legajos de los estudiantes.

    Returns:
        int: Índice del estudiante si se encuentra, -1 si no existe.
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo:
            return i
    return -1

def ordenar_por_promedio(matriz, nombres, generos, legajos, promedios, orden):
    """Ordena estudiantes según su promedio usando método burbuja.

    Args:
        matriz (list[list[int]]): Matriz con las notas de los estudiantes.
        nombres (list[str]): Lista con nombres de los estudiantes.
        generos (list[str]): Lista con géneros de los estudiantes.
        legajos (list[int]): Lista con legajos de los estudiantes.
        promedios (list[float]): Lista con los promedios de cada estudiante.
        orden (str): 'ASC' para ascendente, 'DESC' para descendente.

    Returns:
        list: (matriz, nombres, generos, legajos, promedios) ordenados según promedio.
    """
    n = len(promedios)
    # Método burbuja
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if orden == "ASC":
                if promedios[j] > promedios[j + 1]:
                    promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                    matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                    generos[j], generos[j + 1] = generos[j + 1], generos[j]
                    legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]
            else:
                if promedios[j] < promedios[j + 1]:
                    promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                    matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                    generos[j], generos[j + 1] = generos[j + 1], generos[j]
                    legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]

    return matriz, nombres, generos, legajos, promedios
