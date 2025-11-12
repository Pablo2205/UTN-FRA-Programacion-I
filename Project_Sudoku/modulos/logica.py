"""
================================================================================
MÓDULO: logica.py
DESCRIPCIÓN: Maneja toda la lógica del juego (estado, acciones, puntuación)
             Controla las acciones del jugador y actualiza el estado
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
from modulos.datos import generar_sudoku_jugable
from modulos.validacion import (validar_numero, verificar_zona_completa, 
                                 verificar_matriz_completa, calcular_puntos_zona)
from modulos.configuracion import (PUNTAJE_INICIAL, DESCUENTO_POR_ERROR, 
                                    PUNTOS_COMPLETAR_TABLERO)


# -------------------- FUNCIONES --------------------
def inicializar_juego(dificultad):
    """
    Inicializa un nuevo juego de Sudoku con la dificultad elegida
    
    Parámetros:
        dificultad (str): Nivel ('facil', 'medio', 'dificil')
    
    Operación:
        1. Genera matrices del juego según dificultad
        2. Crea el diccionario de estado inicial
    
    Retorna:
        dict: Estado inicial del juego con todas las variables necesarias
    """
    # Generar matrices del Sudoku
    resultado_generacion = generar_sudoku_jugable(dificultad)
    matriz_juego = resultado_generacion[0]
    matriz_solucion = resultado_generacion[1]
    matriz_fijos = resultado_generacion[2]
    
    # Crear estado inicial
    estado = {
        'matriz_juego': matriz_juego,
        'matriz_solucion': matriz_solucion,
        'matriz_fijos': matriz_fijos,
        'celda_seleccionada': None,
        'puntaje': PUNTAJE_INICIAL,
        'errores': 0,
        'juego_terminado': False,
        'dificultad': dificultad,
        'zonas_completadas': set(),
        'estados_celdas': {},
        'en_menu': False
    }
    
    return estado


def seleccionar_celda(estado, fila, col):
    """
    Selecciona una celda del tablero para editar
    
    Parámetros:
        estado (dict): Estado actual del juego
        fila (int): Número de fila a seleccionar (0-8)
        col (int): Número de columna a seleccionar (0-8)
    
    Operación:
        - Verifica que la celda no sea fija
        - Si es editable, la marca como seleccionada
    
    Retorna:
        bool: True si se pudo seleccionar, False si es celda fija
    """
    celda_es_fija = estado['matriz_fijos'][fila][col]
    
    if celda_es_fija:
        return False
    
    posicion = (fila, col)
    estado['celda_seleccionada'] = posicion
    return True


def colocar_numero(estado, numero):
    """
    Coloca un número en la celda seleccionada
    
    Parámetros:
        estado (dict): Estado actual del juego
        numero (int): Número a colocar (1-9)
    
    Operación:
        1. Verifica que haya una celda seleccionada
        2. Verifica que la celda no sea fija
        3. Valida si el número cumple reglas (no duplicado)
        4. Verifica si coincide con la solución
        5. Actualiza puntuación y estado de la celda
        6. Verifica si se completó alguna zona o el juego
    
    Retorna:
        dict: Resultado con 'exito', 'mensaje', 'puntos', 'tipo'
    """
    # Verificar que hay celda seleccionada
    hay_celda_seleccionada = estado['celda_seleccionada'] is None
    if hay_celda_seleccionada:
        resultado = {
            'exito': False,
            'mensaje': 'No hay celda seleccionada',
            'puntos': 0,
            'tipo': 'normal'
        }
        return resultado
    
    # Obtener posición
    posicion = estado['celda_seleccionada']
    fila = posicion[0]
    col = posicion[1]
    
    # Verificar que no sea celda fija
    celda_es_fija = estado['matriz_fijos'][fila][col]
    if celda_es_fija:
        resultado = {
            'exito': False,
            'mensaje': 'No se puede modificar número fijo',
            'puntos': 0,
            'tipo': 'normal'
        }
        return resultado
    
    # Crear copia temporal para validar
    matriz_temp = []
    for fila_matriz in estado['matriz_juego']:
        fila_copia = fila_matriz[:]
        matriz_temp.append(fila_copia)
    
    matriz_temp[fila][col] = numero
    
    # Validar si el número cumple las reglas (no duplicado)
    numero_es_valido = validar_numero(matriz_temp, fila, col, numero)
    
    if numero_es_valido == False:
        # Número duplicado - colocarlo temporalmente para mostrar en amarillo
        estado['matriz_juego'][fila][col] = numero
        posicion_celda = (fila, col)
        estado['estados_celdas'][posicion_celda] = 'duplicado'
        
        resultado = {
            'exito': False,
            'mensaje': 'Número duplicado en fila/columna/región',
            'puntos': 0,
            'tipo': 'duplicado'
        }
        return resultado
    
    # Verificar si coincide con la solución
    numero_solucion = estado['matriz_solucion'][fila][col]
    numero_es_correcto = numero == numero_solucion
    
    if numero_es_correcto == False:
        # Válido pero incorrecto - descontar puntos
        estado['matriz_juego'][fila][col] = numero
        puntaje_nuevo = estado['puntaje'] - DESCUENTO_POR_ERROR
        
        if puntaje_nuevo < 0:
            puntaje_nuevo = 0
        
        estado['puntaje'] = puntaje_nuevo
        estado['errores'] = estado['errores'] + 1
        
        posicion_celda = (fila, col)
        estado['estados_celdas'][posicion_celda] = 'error'
        
        resultado = {
            'exito': False,
            'mensaje': 'Número incorrecto',
            'puntos': -DESCUENTO_POR_ERROR,
            'tipo': 'error'
        }
        return resultado
    
    # Número correcto - colocarlo
    estado['matriz_juego'][fila][col] = numero
    posicion_celda = (fila, col)
    estado['estados_celdas'][posicion_celda] = 'correcto'
    
    # Verificar zonas completadas
    zonas = verificar_zona_completa(estado['matriz_juego'], fila, col)
    puntos_ganados = 0
    
    # Crear identificadores únicos para cada zona
    id_fila = f"fila_{fila}"
    id_col = f"col_{col}"
    numero_region = (fila // 3) * 3 + (col // 3)
    id_region = f"region_{numero_region}"
    
    # Sumar puntos por zonas completadas (solo la primera vez)
    fila_completa = zonas['fila']
    fila_ya_contada = id_fila in estado['zonas_completadas']
    
    if fila_completa and fila_ya_contada == False:
        estado['zonas_completadas'].add(id_fila)
        puntos_ganados = puntos_ganados + 9
    
    columna_completa = zonas['columna']
    columna_ya_contada = id_col in estado['zonas_completadas']
    
    if columna_completa and columna_ya_contada == False:
        estado['zonas_completadas'].add(id_col)
        puntos_ganados = puntos_ganados + 9
    
    region_completa = zonas['region']
    region_ya_contada = id_region in estado['zonas_completadas']
    
    if region_completa and region_ya_contada == False:
        estado['zonas_completadas'].add(id_region)
        puntos_ganados = puntos_ganados + 9
    
    estado['puntaje'] = estado['puntaje'] + puntos_ganados
    
    # Verificar si completó todo el Sudoku
    tablero_completo = verificar_matriz_completa(estado['matriz_juego'])
    
    if tablero_completo:
        estado['juego_terminado'] = True
        estado['puntaje'] = estado['puntaje'] + PUNTOS_COMPLETAR_TABLERO
        puntos_ganados = puntos_ganados + PUNTOS_COMPLETAR_TABLERO
        
        resultado = {
            'exito': True,
            'mensaje': '¡Felicidades! Completaste el Sudoku',
            'puntos': puntos_ganados,
            'tipo': 'correcto'
        }
        return resultado
    
    # Crear mensaje
    mensaje = 'Número colocado correctamente'
    if puntos_ganados > 0:
        mensaje = mensaje + f' (+{puntos_ganados} pts)'
    
    resultado = {
        'exito': True,
        'mensaje': mensaje,
        'puntos': puntos_ganados,
        'tipo': 'correcto'
    }
    
    return resultado


def borrar_numero(estado):
    """
    Borra el número de la celda seleccionada
    
    Parámetros:
        estado (dict): Estado actual del juego
    
    Operación:
        1. Verifica que haya celda seleccionada
        2. Verifica que no sea celda fija
        3. Borra el número (coloca 0)
        4. Limpia el estado de color de la celda
    
    Retorna:
        bool: True si se pudo borrar, False si no
    """
    # Verificar que hay celda seleccionada
    hay_celda_seleccionada = estado['celda_seleccionada'] is None
    if hay_celda_seleccionada:
        return False
    
    # Obtener posición
    posicion = estado['celda_seleccionada']
    fila = posicion[0]
    col = posicion[1]
    
    # Verificar que no sea celda fija
    celda_es_fija = estado['matriz_fijos'][fila][col]
    if celda_es_fija:
        return False
    
    # Borrar número
    estado['matriz_juego'][fila][col] = 0
    
    # Limpiar estado de la celda
    posicion_celda = (fila, col)
    celda_tiene_estado = posicion_celda in estado['estados_celdas']
    
    if celda_tiene_estado:
        del estado['estados_celdas'][posicion_celda]
    
    return True


def reiniciar_juego(estado):
    """
    Reinicia el juego manteniendo la misma dificultad
    
    Parámetros:
        estado (dict): Estado actual del juego
    
    Operación:
        - Obtiene la dificultad actual
        - Genera un nuevo juego con esa dificultad
    
    Retorna:
        dict: Nuevo estado del juego con mismo nivel
    """
    dificultad_actual = estado['dificultad']
    nuevo_estado = inicializar_juego(dificultad_actual)
    
    return nuevo_estado