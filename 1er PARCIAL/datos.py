'''
 Módulo: modulo_datos.py
    Encargado de definir constantes, validar datos 
    y generar información simulada de estudiantes.


'''

# --------- Constantes generales ----------
NUM_ESTUDIANTES = 30
NUM_MATERIAS = 5

# --------- Funciones de validación ----------

def validar_calificacion(valor):
    """Verifica que la calificación esté dentro del rango 1 a 10."""
    calificacion_valida = valor >= 1 and valor <= 10
    return calificacion_valida


def validar_genero(genero):
    """Verifica que el género sea 'F', 'M' o 'X'."""
    genero_valido = genero in ['F', 'M', 'X']
    return genero_valido


def validar_legajo(legajo):
    """Verifica que el legajo tenga cinco cifras (10000 a 99999)."""
    legajo_valido = legajo >= 10000 and legajo <= 99999
    return legajo_valido


def validar_estado(estado):
    """Verifica que el estado sea 0 (inactivo) o 1 (activo)."""
    estado_valido = estado == 0 or estado == 1
    return estado_valido


def validar_nombre(nombre):
    """Verifica que el nombre no esté vacío."""
    nombre_valido = len(nombre) > 0
    return nombre_valido


# --------- Carga de datos hardcodeados ----------

def crear_datos_hardcodeados():
    """
    Crea datos simulados de 30 estudiantes.
    Cada estudiante tiene:
        - Nombre
        - Género
        - Legajo
        - Estado (activo/inactivo)
        - Notas en 5 materias
    """

    # Lista fija de nombres
    lista_nombres = [
        "García, Juan", "López, María", "Martínez, Carlos", "González, Ana", "Pérez, Luis",
        "Sánchez, Carmen", "Ramírez, Diego", "Torres, Laura", "Flores, Miguel", "Rivera, Sofía",
        "Morales, Andrés", "Jiménez, Elena", "Herrera, Pablo", "Cruz, Isabel", "Reyes, Fernando",
        "Vargas, Patricia", "Mendoza, Roberto", "Silva, Gabriela", "Ortega, Daniel", "Castro, Natalia",
        "Romero, Alejandro", "Moreno, Valeria", "Álvarez, Sebastián", "Gutiérrez, Camila", "Ruiz, Nicolás",
        "Díaz, Andrea", "Hernández, Martín", "Muñoz, Daniela", "Aguilar, Santiago", "Vega, Lucía"
    ]

    generos_posibles = ['F', 'M', 'X']

    # Inicializamos listas de tamaño fijo
    matriz_notas = [[0 for materia in range(NUM_MATERIAS)] for estudiante in range(NUM_ESTUDIANTES)]
    lista_generos = [0] * NUM_ESTUDIANTES
    lista_legajos = [0] * NUM_ESTUDIANTES
    lista_estados = [0] * NUM_ESTUDIANTES

    # Asignamos los datos
    for indice_estudiante in range(NUM_ESTUDIANTES):
        # Notas de cada materia
        for indice_materia in range(NUM_MATERIAS):
            matriz_notas[indice_estudiante][indice_materia] = ((indice_estudiante + indice_materia) % 10) + 1

        # Género
        lista_generos[indice_estudiante] = generos_posibles[indice_estudiante % 3]

        # Legajo
        lista_legajos[indice_estudiante] = 100000 + indice_estudiante

        # Estado: 2 de cada 3 estudiantes activos
        lista_estados[indice_estudiante] = 1 if indice_estudiante % 3 != 0 else 0

    return matriz_notas, lista_nombres, lista_generos, lista_legajos, lista_estados

