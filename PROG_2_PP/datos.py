# --------- Constantes generales ----------
NUM_ESTUDIANTES = 30
NUM_MATERIAS = 5

# --------- Funciones de validación ----------

def validar_calificacion(valor):
    """Valida si una calificación está entre 1 y 10.

    Args:
        valor (int): Calificación a validar.

    Returns:
        bool: True si está entre 1 y 10, False si no.
    """
    calificacion_valida = valor >= 1 and valor <= 10
    return calificacion_valida

def validar_genero(genero):
    """Valida si un género es 'F', 'M' o 'X'.

    Args:
        genero (str): Género a validar.

    Returns:
        bool: True si es válido, False si no.
    """
    genero_valido = genero in ['F', 'M', 'X']
    return genero_valido

def validar_legajo(legajo):
    """Valida si un legajo tiene cinco cifras (10000 a 99999).

    Args:
        legajo (int): Legajo a validar.

    Returns:
        bool: True si es válido, False si no.
    """    
    legajo_valido = legajo >= 10000 and legajo <= 99999
    return legajo_valido

def validar_nombre(nombre):
    """Valida que un nombre no esté vacío.

    Args:
        nombre (str): Nombre a validar.

    Returns:
        bool: True si no está vacío, False si lo está.
    """
    nombre_valido = len(nombre) > 0
    return nombre_valido

# --------- Carga de datos hardcodeados ----------

def crear_datos_hardcodeados():
    """
    Crea datos simulados de 30 estudiantes en listas.

    Returns:
        list: Contiene cinco listas:
            - matriz_notas: matriz de notas de cada estudiante
            - lista_nombres: lista de nombres
            - lista_generos: lista de géneros
            - lista_legajos: lista de legajos
            - lista_estados: lista de estados (todos activos)
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
    lista_estados = [1] * NUM_ESTUDIANTES  # Todos activos

    # Asignamos los datos
    for indice_estudiante in range(NUM_ESTUDIANTES):
        # Notas de cada materia
        for indice_materia in range(NUM_MATERIAS):
            matriz_notas[indice_estudiante][indice_materia] = ((indice_estudiante + indice_materia) % 10) + 1

        lista_generos[indice_estudiante] = generos_posibles[indice_estudiante % 3]
        lista_legajos[indice_estudiante] = 100000 + indice_estudiante
        # print(matriz_notas)  # Lo hago para probar salida de matriz (ya se que está prohibido)

    return [matriz_notas, lista_nombres, lista_generos, lista_legajos]


















def crear_datos_manualmente():
    """
    Permite al usuario ingresar datos de estudiantes manualmente.

    Returns:
        list: Contiene cinco listas:
            - matriz_notas: matriz de notas de cada estudiante
            - lista_nombres: lista de nombres
            - lista_generos: lista de géneros
            - lista_legajos: lista de legajos
            - lista_estados: lista de estados (todos activos)
    """

    # Preguntar cuántos estudiantes se van a cargar
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    cantidad_materias = 5  # fija como en tu proyecto

    # Inicializar listas
    matriz_notas = [[0 for j in range(cantidad_materias)] for i in range(cantidad_estudiantes)]
    lista_nombres = [0] * cantidad_estudiantes
    lista_generos = [0] * cantidad_estudiantes
    lista_legajos = [0] * cantidad_estudiantes

    # Ingreso de datos
    for i in range(cantidad_estudiantes):
        print("Ingresando datos del estudiante", i + 1)
        lista_nombres[i] = input("  Nombre: ")
        lista_generos[i] = input("  Género (F/M/X): ")
        lista_legajos[i] = int(input("  Legajo: "))

        # Notas
        for j in range(cantidad_materias):
            matriz_notas[i][j] = int(input("    Nota de materia " + str(j + 1) + ": "))

    # Todos activos
    lista_estados = [1] * cantidad_estudiantes

    return matriz_notas, lista_nombres, lista_generos, lista_legajos, lista_estados


