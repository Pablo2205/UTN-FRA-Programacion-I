
# Cálculo de promedios y conteos de notas
def calcular_promedio_estudiante(lista_notas):
    """Calcula el promedio de un estudiante.

    Args:
        lista_notas (list[int]): Lista de notas del estudiante.

    Returns:
        float: Promedio del estudiante.
    """    
    suma_notas = 0
    cantidad_notas = len(lista_notas)

    for nota in lista_notas:
        suma_notas = suma_notas + nota

    promedio = suma_notas / cantidad_notas
    return promedio

# Calcula el promedio de cada estudiante
def calcular_promedios(matriz_notas):
    """Calcula los promedios de todos los estudiantes.

    Args:
        matriz_notas (list[list[int]]): Matriz con las notas de todos los estudiantes.

    Returns:
        list[float]: Lista con los promedios de cada estudiante.
    """
    cantidad_estudiantes = len(matriz_notas)
    lista_promedios = [0] * cantidad_estudiantes

    # Recorro todos los estudiantes
    for i in range(cantidad_estudiantes):
        promedio_estudiante = calcular_promedio_estudiante(matriz_notas[i])
        lista_promedios[i] = promedio_estudiante

    return lista_promedios

# Calcula las materias con mayor promedio
def mejores_materias(matriz_notas):
    """Encuentra las materias con mayor promedio.

    Args:
        matriz_notas (list[list[int]]): Matriz con las notas de todos los estudiantes.

    Returns:
        list: 
            Contiene dos listas:
                [0] -> índices de las materias con mayor promedio
                [1] -> promedios de todas las materias
    """

    cantidad_materias = len(matriz_notas[0])
    lista_promedios_materias = [0] * cantidad_materias

    # Calculo el promedio general de cada materia
    for j in range(cantidad_materias):
        suma_notas = 0
        cantidad_estudiantes = len(matriz_notas)

        for i in range(cantidad_estudiantes):
            suma_notas = suma_notas + matriz_notas[i][j]

        promedio_materia = suma_notas / cantidad_estudiantes
        lista_promedios_materias[j] = promedio_materia

    # Busco el valor máximo de los promedios
    mayor_promedio = lista_promedios_materias[0]
    for promedio in lista_promedios_materias:
        if promedio > mayor_promedio:
            mayor_promedio = promedio

    # Creo la lista de índices de materias con ese promedio
    cantidad_mejores = 0
    for j in range(cantidad_materias):
        if lista_promedios_materias[j] == mayor_promedio:
            cantidad_mejores = cantidad_mejores + 1

    lista_indices_mejores = [0] * cantidad_mejores
    indice_actual = 0
    for j in range(cantidad_materias):
        if lista_promedios_materias[j] == mayor_promedio:
            lista_indices_mejores[indice_actual] = j
            indice_actual = indice_actual + 1

    return [lista_indices_mejores, lista_promedios_materias]


# Cuento cuántas veces se repite cada nota (1 a 10) en una materia específica
def contar_notas_por_materia(matriz_notas, indice_materia):
    """Cuenta cuántas veces se repite cada nota en una materia.

    Args:
        matriz_notas (list[list[int]]): Matriz con las notas de todos los estudiantes.
        indice_materia (int): Índice de la materia a analizar.

    Returns:
        list[int]: Lista con la cantidad de veces que aparece cada nota (1-10).
    """
    conteo_notas = [0] * 10  # Inicializamos una lista con 10 ceros

    # Recorro todos los estudiantes (todos activos)
    for i in range(len(matriz_notas)):
        nota = matriz_notas[i][indice_materia]
        posicion = nota - 1
        conteo_notas[posicion] += 1

    return conteo_notas
