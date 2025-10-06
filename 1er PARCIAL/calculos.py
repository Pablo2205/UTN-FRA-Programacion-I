# modulo_calculos.py
# =====================================
# Este módulo contiene funciones relacionadas con los cálculos del sistema:
# - Calcular promedios individuales y generales.
# - Determinar las materias con mejor promedio.
# - Contar la frecuencia de notas en una materia específica.
# =====================================


def calcular_promedio_estudiante(lista_notas):
    """
    Calcula el promedio de un estudiante a partir de su lista de notas.
    """
    suma_notas = 0
    cantidad_notas = len(lista_notas)

    for nota in lista_notas:
        suma_notas = suma_notas + nota

    promedio = suma_notas / cantidad_notas
    return promedio



def calcular_promedios(matriz_notas, lista_estados):
    """
    Calcula el promedio de cada estudiante activo (estado = 1)
    y devuelve una lista con todos los promedios.
    """
    cantidad_estudiantes = len(matriz_notas)
    lista_promedios = [0] * cantidad_estudiantes

    for i in range(cantidad_estudiantes):
        if lista_estados[i] == 1:
            promedio_estudiante = calcular_promedio_estudiante(matriz_notas[i])
            lista_promedios[i] = promedio_estudiante

    return lista_promedios



def mejores_materias(matriz_notas, lista_estados):
    """
    Calcula el promedio general de cada materia (columna de la matriz)
    y determina cuál o cuáles tienen el promedio más alto.
    Devuelve:
      - lista_indices_mejores: índices de las materias con mayor promedio.
      - lista_promedios_materias: promedios generales de todas las materias.
    """

    cantidad_materias = len(matriz_notas[0])
    lista_promedios_materias = [0] * cantidad_materias

    # Paso 1: Calcular el promedio general de cada materia
    for j in range(cantidad_materias):
        suma_notas = 0
        contador_activos = 0

        for i in range(len(matriz_notas)):
            if lista_estados[i] == 1:
                suma_notas = suma_notas + matriz_notas[i][j]
                contador_activos = contador_activos + 1

        if contador_activos != 0:
            promedio_materia = suma_notas / contador_activos
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
            lista_indices_mejores = lista_indices_mejores + [j]

    return lista_indices_mejores, lista_promedios_materias



def contar_notas_por_materia(matriz_notas, indice_materia, lista_estados):
    """
    Cuenta cuántas veces se repite cada nota (del 1 al 10)
    en una materia específica (columna).
    Devuelve una lista de 10 posiciones donde:
      - el índice 0 = cantidad de notas 1
      - el índice 1 = cantidad de notas 2
      - ...
      - el índice 9 = cantidad de notas 10
    """

    conteo_notas = [0] * 10  # Inicializamos una lista con 10 ceros

    for i in range(len(matriz_notas)):
        if lista_estados[i] == 1:
            nota = matriz_notas[i][indice_materia]
            posicion = nota - 1
            conteo_notas[posicion] = conteo_notas[posicion] + 1

    return conteo_notas
