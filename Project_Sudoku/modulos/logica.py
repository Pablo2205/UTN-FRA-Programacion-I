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
                                 verificar_matriz_completa)
from modulos.configuracion import (PUNTAJE_INICIAL, DESCUENTO_POR_ERROR, 
                                    PUNTOS_COMPLETAR_TABLERO, PUNTOS_ZONA_COMPLETA)


# -------------------- FUNCIONES --------------------
def inicializar_juego(dificultad, nombre_jugador=""):
    """
    Inicializa un nuevo juego de Sudoku con la dificultad elegida
    
    Parámetros:
        dificultad (str): Nivel ('facil', 'medio', 'dificil')
        nombre_jugador (str): Nombre del jugador
    
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
        'en_menu': False,
        'nombre_jugador': nombre_jugador,
        'tiempo_inicio': 0  # Se setea cuando empieza a jugar
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
    Coloca un número en la celda seleccionada (SIN validar corrección)
    
    Parámetros:
        estado (dict): Estado actual del juego
        numero (int): Número a colocar (1-9)
    
    Operación:
        1. Verifica que haya una celda seleccionada
        2. Verifica que la celda no sea fija
        3. Valida solo si el número es duplicado (reglas de Sudoku)
        4. Si NO es duplicado, lo coloca (sin verificar si es correcto)
        5. La validación de corrección se hace SOLO al presionar "Validar"
    
    Retorna:
        dict: Resultado con 'exito', 'mensaje', 'tipo'
    """
    # Verificar que hay celda seleccionada
    hay_celda_seleccionada = estado['celda_seleccionada'] is None
    if hay_celda_seleccionada:
        resultado = {
            'exito': False,
            'mensaje': 'No hay celda seleccionada',
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
            'tipo': 'normal'
        }
        return resultado
    
    # Crear copia temporal para validar duplicados
    matriz_temp = []
    for fila_matriz in estado['matriz_juego']:
        fila_copia = fila_matriz[:]
        matriz_temp.append(fila_copia)
    
    matriz_temp[fila][col] = numero
    
    # Validar SOLO si es duplicado (no verificar corrección)
    numero_es_valido = validar_numero(matriz_temp, fila, col, numero)
    
    if numero_es_valido == False:
        # Número duplicado - no se puede colocar
        resultado = {
            'exito': False,
            'mensaje': 'Número duplicado en fila/columna/región',
            'tipo': 'duplicado'
        }
        return resultado
    
    # Número válido (no duplicado) - colocarlo SIN verificar corrección
    estado['matriz_juego'][fila][col] = numero
    
    # Limpiar estado de colores (se aplicarán al validar)
    posicion_celda = (fila, col)
    if posicion_celda in estado['estados_celdas']:
        del estado['estados_celdas'][posicion_celda]
    
    resultado = {
        'exito': True,
        'mensaje': 'Número colocado',
        'tipo': 'colocado'
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


def validar_y_calcular_puntaje(estado):
    """
    Valida toda la matriz, aplica colores y calcula puntaje
    
    Parámetros:
        estado (dict): Estado actual del juego
    
    Operación:
        1. Compara cada celda con la solución
        2. Aplica colores (verde=correcto, rojo=incorrecto)
        3. Calcula descuentos por errores
        4. Calcula bonificaciones por zonas completas
        5. Verifica si completó el tablero
    
    Retorna:
        dict: Resultado con puntaje final y estadísticas
    """
    # Limpiar estados anteriores
    estado['estados_celdas'] = {}
    estado['zonas_completadas'] = set()
    
    correctas = 0
    incorrectas = 0
    vacias = 0
    
    # Validar cada celda
    for fila in range(9):
        for col in range(9):
            celda_es_fija = estado['matriz_fijos'][fila][col]
            
            if celda_es_fija == False:
                valor_jugador = estado['matriz_juego'][fila][col]
                valor_solucion = estado['matriz_solucion'][fila][col]
                
                if valor_jugador == 0:
                    vacias = vacias + 1
                else:
                    numero_es_correcto = valor_jugador == valor_solucion
                    
                    if numero_es_correcto:
                        correctas = correctas + 1
                        posicion = (fila, col)
                        estado['estados_celdas'][posicion] = 'correcto'
                    else:
                        incorrectas = incorrectas + 1
                        posicion = (fila, col)
                        estado['estados_celdas'][posicion] = 'error'
    
    # Calcular puntaje
    puntaje = 0
    
    # Descontar por errores
    descuento = incorrectas * DESCUENTO_POR_ERROR
    puntaje = puntaje - descuento
    
    # Bonificaciones por zonas completas (solo las correctas)
    for fila in range(9):
        fila_completa_correcta = True
        
        for col in range(9):
            valor_jugador = estado['matriz_juego'][fila][col]
            valor_solucion = estado['matriz_solucion'][fila][col]
            
            if valor_jugador == 0 or valor_jugador != valor_solucion:
                fila_completa_correcta = False
                break
        
        if fila_completa_correcta:
            puntaje = puntaje + PUNTOS_ZONA_COMPLETA
            id_fila = f"fila_{fila}"
            estado['zonas_completadas'].add(id_fila)
    
    # Verificar columnas completas
    for col in range(9):
        columna_completa_correcta = True
        
        for fila in range(9):
            valor_jugador = estado['matriz_juego'][fila][col]
            valor_solucion = estado['matriz_solucion'][fila][col]
            
            if valor_jugador == 0 or valor_jugador != valor_solucion:
                columna_completa_correcta = False
                break
        
        if columna_completa_correcta:
            puntaje = puntaje + PUNTOS_ZONA_COMPLETA
            id_col = f"col_{col}"
            estado['zonas_completadas'].add(id_col)
    
    # Verificar regiones completas
    for region_fila in range(3):
        for region_col in range(3):
            region_completa_correcta = True
            
            for f in range(region_fila * 3, region_fila * 3 + 3):
                for c in range(region_col * 3, region_col * 3 + 3):
                    valor_jugador = estado['matriz_juego'][f][c]
                    valor_solucion = estado['matriz_solucion'][f][c]
                    
                    if valor_jugador == 0 or valor_jugador != valor_solucion:
                        region_completa_correcta = False
                        break
                
                if region_completa_correcta == False:
                    break
            
            if region_completa_correcta:
                puntaje = puntaje + PUNTOS_ZONA_COMPLETA
                numero_region = region_fila * 3 + region_col
                id_region = f"region_{numero_region}"
                estado['zonas_completadas'].add(id_region)
    
    # Verificar si completó TODO correctamente
    tablero_completo = verificar_matriz_completa(estado['matriz_juego'])
    
    if tablero_completo:
        puntaje = puntaje + PUNTOS_COMPLETAR_TABLERO
        estado['juego_terminado'] = True
    
    # Actualizar puntaje en el estado
    estado['puntaje'] = puntaje
    
    resultado = {
        'puntaje_final': puntaje,
        'correctas': correctas,
        'incorrectas': incorrectas,
        'vacias': vacias,
        'completo': tablero_completo
    }
    
    return resultado