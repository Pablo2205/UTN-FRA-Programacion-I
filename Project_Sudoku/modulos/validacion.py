"""
================================================================================
MÓDULO: validacion.py
DESCRIPCIÓN: Valida números, verifica zonas completas y calcula puntuación
             Comprueba si el jugador está colocando números correctamente
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
from modulos.configuracion import (TAMANO_TABLERO, PUNTOS_ZONA_COMPLETA, 
                                    PUNTOS_COMPLETAR_TABLERO)


# -------------------- FUNCIONES --------------------
def validar_numero(matriz, fila, col, num):
    """
    Valida si un número colocado cumple las reglas del Sudoku
    
    Parámetros:
        matriz (list): Matriz actual del juego
        fila (int): Número de fila donde se colocó (0-8)
        col (int): Número de columna donde se colocó (0-8)
        num (int): Número a validar (1-9)
    
    Operación:
        1. Verifica que el número esté entre 1 y 9
        2. Verifica que no haya duplicados en la fila
        3. Verifica que no haya duplicados en la columna
        4. Verifica que no haya duplicados en la región 3x3
    
    Retorna:
        bool: True si el número es válido, False si no cumple las reglas
    """
    # Verificar rango válido
    numero_es_valido = num >= 1 and num <= 9
    if numero_es_valido == False:
        return False
    
    # Verificar duplicados en la fila (sin contar la posición actual)
    for c in range(TAMANO_TABLERO):
        es_misma_columna = c == col
        if es_misma_columna:
            continue
        
        valor_celda = matriz[fila][c]
        hay_duplicado = valor_celda == num
        if hay_duplicado:
            return False
    
    # Verificar duplicados en la columna (sin contar la posición actual)
    for f in range(TAMANO_TABLERO):
        es_misma_fila = f == fila
        if es_misma_fila:
            continue
        
        valor_celda = matriz[f][col]
        hay_duplicado = valor_celda == num
        if hay_duplicado:
            return False
    
    # Calcular inicio de la región 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    
    # Verificar duplicados en la región 3x3
    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            es_misma_celda = (f == fila and c == col)
            if es_misma_celda:
                continue
            
            valor_celda = matriz[f][c]
            hay_duplicado = valor_celda == num
            if hay_duplicado:
                return False
    
    return True


def verificar_zona_completa(matriz, fila, col):
    """
    Verifica si una fila, columna o región está completa y correcta
    
    Parámetros:
        matriz (list): Matriz del juego actual
        fila (int): Fila de referencia (0-8)
        col (int): Columna de referencia (0-8)
    
    Operación:
        1. Verifica si la fila está completa (1-9 sin repetir)
        2. Verifica si la columna está completa (1-9 sin repetir)
        3. Verifica si la región 3x3 está completa (1-9 sin repetir)
    
    Retorna:
        dict: Diccionario con claves 'fila', 'columna', 'region'
              Cada una es True si está completa y correcta
    """
    resultado = {
        'fila': False,
        'columna': False,
        'region': False
    }
    
    # Verificar fila completa
    fila_tiene_ceros = False
    for c in range(TAMANO_TABLERO):
        valor = matriz[fila][c]
        if valor == 0:
            fila_tiene_ceros = True
            break
    
    if fila_tiene_ceros == False:
        # Verificar que tenga todos los números del 1 al 9
        numeros_fila = set(matriz[fila])
        numeros_esperados = set(range(1, 10))
        fila_es_correcta = numeros_fila == numeros_esperados
        resultado['fila'] = fila_es_correcta
    
    # Verificar columna completa
    columna_tiene_ceros = False
    for f in range(TAMANO_TABLERO):
        valor = matriz[f][col]
        if valor == 0:
            columna_tiene_ceros = True
            break
    
    if columna_tiene_ceros == False:
        # Verificar que tenga todos los números del 1 al 9
        numeros_columna = []
        for f in range(TAMANO_TABLERO):
            numero = matriz[f][col]
            numeros_columna.append(numero)
        
        numeros_columna_set = set(numeros_columna)
        numeros_esperados = set(range(1, 10))
        columna_es_correcta = numeros_columna_set == numeros_esperados
        resultado['columna'] = columna_es_correcta
    
    # Verificar región 3x3 completa
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    
    numeros_region = []
    region_tiene_ceros = False
    
    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            valor = matriz[f][c]
            if valor == 0:
                region_tiene_ceros = True
                break
            numeros_region.append(valor)
        
        if region_tiene_ceros:
            break
    
    if region_tiene_ceros == False:
        numeros_region_set = set(numeros_region)
        numeros_esperados = set(range(1, 10))
        region_es_correcta = numeros_region_set == numeros_esperados
        resultado['region'] = region_es_correcta
    
    return resultado


def verificar_matriz_completa(matriz):
    """
    Verifica si todo el Sudoku está completo y correcto
    
    Parámetros:
        matriz (list): Matriz del juego a verificar
    
    Operación:
        1. Verifica que no haya celdas vacías
        2. Verifica que todas las filas tengan números del 1 al 9
        3. Verifica que todas las columnas tengan números del 1 al 9
        4. Verifica que todas las regiones tengan números del 1 al 9
    
    Retorna:
        bool: True si el Sudoku está completo y correcto
    """
    # Verificar que no haya celdas vacías
    for fila in range(TAMANO_TABLERO):
        for col in range(TAMANO_TABLERO):
            valor = matriz[fila][col]
            if valor == 0:
                return False
    
    # Verificar todas las filas
    for fila in range(TAMANO_TABLERO):
        numeros_fila = set(matriz[fila])
        numeros_esperados = set(range(1, 10))
        fila_es_correcta = numeros_fila == numeros_esperados
        
        if fila_es_correcta == False:
            return False
    
    # Verificar todas las columnas
    for col in range(TAMANO_TABLERO):
        numeros_columna = []
        for fila in range(TAMANO_TABLERO):
            numero = matriz[fila][col]
            numeros_columna.append(numero)
        
        numeros_columna_set = set(numeros_columna)
        numeros_esperados = set(range(1, 10))
        columna_es_correcta = numeros_columna_set == numeros_esperados
        
        if columna_es_correcta == False:
            return False
    
    # Verificar todas las regiones
    for region_fila in range(3):
        for region_col in range(3):
            numeros_region = []
            
            for f in range(region_fila * 3, region_fila * 3 + 3):
                for c in range(region_col * 3, region_col * 3 + 3):
                    numero = matriz[f][c]
                    numeros_region.append(numero)
            
            numeros_region_set = set(numeros_region)
            numeros_esperados = set(range(1, 10))
            region_es_correcta = numeros_region_set == numeros_esperados
            
            if region_es_correcta == False:
                return False
    
    return True


def validar_solucion(estado):
    """
    Valida la solución actual comparándola con la solución correcta
    
    Parámetros:
        estado (dict): Estado actual del juego con matrices
    
    Operación:
        1. Compara cada celda no fija con la solución correcta
        2. Cuenta celdas correctas, incorrectas y vacías
    
    Retorna:
        dict: Diccionario con información de validación:
            - 'correcta': True si todo está bien
            - 'celdas_incorrectas': Lista de posiciones incorrectas
            - 'celdas_correctas': Lista de posiciones correctas
            - 'total_incorrectas': Cantidad de números incorrectos
            - 'total_correctas': Cantidad de números correctos
            - 'total_vacias': Cantidad de celdas vacías
    """
    celdas_incorrectas = []
    celdas_correctas = []
    total_vacias = 0
    
    for fila in range(9):
        for col in range(9):
            # Solo validar celdas que el jugador puede modificar
            celda_es_fija = estado['matriz_fijos'][fila][col]
            
            if celda_es_fija == False:
                valor_jugador = estado['matriz_juego'][fila][col]
                valor_solucion = estado['matriz_solucion'][fila][col]
                
                celda_esta_vacia = valor_jugador == 0
                
                if celda_esta_vacia:
                    total_vacias = total_vacias + 1
                else:
                    numero_es_correcto = valor_jugador == valor_solucion
                    
                    if numero_es_correcto:
                        posicion = (fila, col)
                        celdas_correctas.append(posicion)
                    else:
                        posicion = (fila, col)
                        celdas_incorrectas.append(posicion)
    
    # Verificar si la solución está completa y correcta
    hay_incorrectas = len(celdas_incorrectas) == 0
    hay_vacias = total_vacias == 0
    solucion_correcta = hay_incorrectas and hay_vacias
    
    resultado = {
        'correcta': solucion_correcta,
        'celdas_incorrectas': celdas_incorrectas,
        'celdas_correctas': celdas_correctas,
        'total_incorrectas': len(celdas_incorrectas),
        'total_correctas': len(celdas_correctas),
        'total_vacias': total_vacias
    }
    
    return resultado


def calcular_puntos_zona(zonas_completas):
    """
    Calcula los puntos obtenidos por completar zonas
    
    Parámetros:
        zonas_completas (dict): Diccionario con zonas completadas
    
    Operación:
        - Suma puntos por cada zona completa (fila, columna, región)
    
    Retorna:
        int: Total de puntos ganados
    """
    puntos = 0
    
    fila_completa = zonas_completas['fila']
    if fila_completa:
        puntos = puntos + PUNTOS_ZONA_COMPLETA
    
    columna_completa = zonas_completas['columna']
    if columna_completa:
        puntos = puntos + PUNTOS_ZONA_COMPLETA
    
    region_completa = zonas_completas['region']
    if region_completa:
        puntos = puntos + PUNTOS_ZONA_COMPLETA
    
    return puntos