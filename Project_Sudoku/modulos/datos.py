"""
================================================================================
MÓDULO: datos.py
DESCRIPCIÓN: Gestiona la generación y manipulación de datos del Sudoku
             Genera matrices, valida números y resuelve el Sudoku
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
import random
from modulos.configuracion import TAMANO_TABLERO, DIFICULTAD


# -------------------- FUNCIONES --------------------
def generar_matriz_vacia():
    """
    Crea una matriz de 9x9 inicializada con ceros
    
    Operación:
        - Crea 9 listas (filas) con 9 ceros cada una
    
    Retorna:
        list: Matriz 9x9 llena de ceros
    """
    matriz = []
    for fila in range(TAMANO_TABLERO):
        fila_nueva = []
        for columna in range(TAMANO_TABLERO):
            fila_nueva.append(0)
        matriz.append(fila_nueva)
    
    return matriz


def es_valido(matriz, fila, col, num):
    """
    Verifica si un número puede colocarse en una posición específica
    
    Parámetros:
        matriz (list): Matriz del Sudoku a validar
        fila (int): Número de fila (0-8)
        col (int): Número de columna (0-8)
        num (int): Número a validar (1-9)
    
    Operación:
        1. Verifica que el número no esté en la misma fila
        2. Verifica que el número no esté en la misma columna
        3. Verifica que el número no esté en la misma región 3x3
    
    Retorna:
        bool: True si el número es válido, False si no lo es
    """
    # Verificar si el número ya está en la fila
    esta_en_fila = num in matriz[fila]
    if esta_en_fila:
        return False
    
    # Verificar si el número ya está en la columna
    for f in range(TAMANO_TABLERO):
        valor_celda = matriz[f][col]
        if valor_celda == num:
            return False
    
    # Calcular el inicio de la región 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    
    # Verificar si el número ya está en la región 3x3
    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            valor_celda = matriz[f][c]
            if valor_celda == num:
                return False
    
    return True


def resolver_sudoku(matriz):
    """
    Resuelve un Sudoku usando el algoritmo de backtracking
    
    Parámetros:
        matriz (list): Matriz del Sudoku a resolver
    
    Operación:
        1. Busca celdas vacías (con valor 0)
        2. Intenta colocar números del 1 al 9 aleatoriamente
        3. Si un número es válido, lo coloca y continúa
        4. Si no encuentra solución, retrocede (backtracking)
    
    Retorna:
        bool: True si se pudo resolver, False si no tiene solución
    """
    for fila in range(TAMANO_TABLERO):
        for col in range(TAMANO_TABLERO):
            valor_actual = matriz[fila][col]
            
            if valor_actual == 0:
                # Crear lista de números 1-9 y mezclarlos
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                
                # Probar cada número
                for num in numeros:
                    numero_es_valido = es_valido(matriz, fila, col, num)
                    
                    if numero_es_valido:
                        matriz[fila][col] = num
                        
                        # Intentar resolver el resto del Sudoku
                        se_resolvio = resolver_sudoku(matriz)
                        if se_resolvio:
                            return True
                        
                        # Si no funcionó, volver a 0 (backtracking)
                        matriz[fila][col] = 0
                
                # No se encontró solución para esta celda
                return False
    
    # Todas las celdas están llenas
    return True


def generar_sudoku_completo():
    """
    Genera un Sudoku completamente resuelto y válido
    
    Operación:
        1. Crea una matriz vacía
        2. La resuelve usando backtracking
    
    Retorna:
        list: Matriz 9x9 con un Sudoku completo y válido
    """
    matriz = generar_matriz_vacia()
    resolver_sudoku(matriz)
    return matriz


def generar_sudoku_jugable(dificultad):
    """
    Genera un Sudoku con números iniciales según la dificultad
    
    Parámetros:
        dificultad (str): Nivel de dificultad ('facil', 'medio', 'dificil')
    
    Operación:
        1. Genera un Sudoku completo (solución)
        2. Copia la solución para crear el tablero de juego
        3. Selecciona números aleatorios para dejar visibles según dificultad
        4. Oculta el resto de números (los pone en 0)
    
    Retorna:
        tuple: (matriz_juego, matriz_solucion, matriz_fijos)
            - matriz_juego: Tablero con algunos números visibles
            - matriz_solucion: Tablero completo resuelto
            - matriz_fijos: Matriz booleana (True = número fijo del sistema)
    """
    # Generar solución completa
    solucion = generar_sudoku_completo()
    
    # Copiar solución para crear el tablero de juego
    juego = []
    for fila in solucion:
        fila_copia = fila[:]
        juego.append(fila_copia)
    
    # Crear matriz para marcar números fijos
    fijos = []
    for fila in range(TAMANO_TABLERO):
        fila_fijos = []
        for col in range(TAMANO_TABLERO):
            fila_fijos.append(False)
        fijos.append(fila_fijos)
    
    # Obtener cantidad de números por región según dificultad
    nums_por_region = DIFICULTAD.get(dificultad, DIFICULTAD['medio'])
    
    # Para cada región 3x3
    for region_fila in range(3):
        for region_col in range(3):
            # Obtener todas las posiciones de esta región
            posiciones = []
            for f in range(region_fila * 3, region_fila * 3 + 3):
                for c in range(region_col * 3, region_col * 3 + 3):
                    posicion = (f, c)
                    posiciones.append(posicion)
            
            # Mezclar y seleccionar posiciones para números fijos
            random.shuffle(posiciones)
            posiciones_fijas = posiciones[:nums_por_region]
            
            # Marcar posiciones fijas y ocultar las demás
            for f in range(region_fila * 3, region_fila * 3 + 3):
                for c in range(region_col * 3, region_col * 3 + 3):
                    posicion_actual = (f, c)
                    es_posicion_fija = posicion_actual in posiciones_fijas
                    
                    if es_posicion_fija:
                        fijos[f][c] = True
                    else:
                        juego[f][c] = 0
    
    return juego, solucion, fijos


def obtener_region(fila, col):
    """
    Calcula el número de región (0-8) para una celda dada
    
    Parámetros:
        fila (int): Número de fila (0-8)
        col (int): Número de columna (0-8)
    
    Operación:
        - Las regiones se numeran de 0 a 8, de izquierda a derecha y arriba abajo
        - Región = (fila // 3) * 3 + (col // 3)
    
    Retorna:
        int: Número de región (0-8)
    """
    numero_fila_region = fila // 3
    numero_col_region = col // 3
    numero_region = numero_fila_region * 3 + numero_col_region
    
    return numero_region