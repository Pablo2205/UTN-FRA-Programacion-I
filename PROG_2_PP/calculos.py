
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

    # Recorro todos los estudiantes (todos están activos)
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
        List:
            list[int]: Índices de las materias con mayor promedio.
            list[float]: Promedios de todas las materias.
    """
    cantidad_materias = len(matriz_notas[0])
    lista_promedios_materias = [0] * cantidad_materias

    # Paso 1: Calcular el promedio general de cada materia
    for j in range(cantidad_materias):
        suma_notas = 0
        cantidad_estudiantes = len(matriz_notas)

        for i in range(cantidad_estudiantes):
            suma_notas += matriz_notas[i][j]  # Sumo la nota de la materia j

        # Calculo el promedio de la materia j
        promedio_materia = suma_notas / cantidad_estudiantes
        lista_promedios_materias[j] = promedio_materia

    # Paso 2: Buscar el valor máximo de los promedios
    mayor_promedio = lista_promedios_materias[0]
    for promedio in lista_promedios_materias:
        if promedio > mayor_promedio:
            mayor_promedio = promedio

    # Paso 3: Obtener los índices de las materias con ese promedio máximo
    lista_indices_mejores = []
    for j in range(cantidad_materias):
        if lista_promedios_materias[j] == mayor_promedio:
            lista_indices_mejores.append(j)

    # Devuelvo los índices y los promedios de todas las materias
    return lista_indices_mejores, lista_promedios_materias


# Cuenta cuántas veces se repite cada nota (1 a 10) en una materia específica
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
