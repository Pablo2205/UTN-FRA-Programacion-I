"""
================================================================================
MÓDULO: interfaz.py
DESCRIPCIÓN: Maneja toda la interfaz gráfica del juego con Pygame
             Dibuja el tablero, botones, menús y mensajes
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
import pygame
import os
from modulos.configuracion import *


# -------------------- FUNCIONES --------------------
def cargar_imagen_fondo():
    """
    Carga la imagen del logo UTN si existe en la carpeta assets
    
    Operación:
        1. Verifica si existe el archivo
        2. Carga la imagen
        3. La escala al tamaño de la ventana
        4. Aplica opacidad configurada
    
    Retorna:
        Surface o None: Imagen cargada con opacidad, o None si no existe
    """
    archivo_existe = os.path.exists(RUTA_IMAGEN_FONDO)
    
    if archivo_existe == False:
        return None
    
    imagen = pygame.image.load(RUTA_IMAGEN_FONDO)
    tamano = (ANCHO_VENTANA, ALTO_VENTANA)
    imagen_escalada = pygame.transform.scale(imagen, tamano)
    imagen_escalada.set_alpha(OPACIDAD_FONDO)
    
    return imagen_escalada


def inicializar_pygame():
    """
    Inicializa Pygame y crea la ventana del juego
    
    Operación:
        1. Inicializa Pygame
        2. Crea la ventana con dimensiones configuradas
        3. Establece el título de la ventana
        4. Crea el reloj para controlar FPS
        5. Carga la imagen de fondo
    
    Retorna:
        tuple: (pantalla, reloj, imagen_fondo)
    """
    pygame.init()
    
    dimensiones = (ANCHO_VENTANA, ALTO_VENTANA)
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption(TITULO)
    
    reloj = pygame.time.Clock()
    imagen_fondo = cargar_imagen_fondo()
    
    return pantalla, reloj, imagen_fondo


def dibujar_tablero(pantalla, estado, imagen_fondo):
    """
    Dibuja el tablero de Sudoku completo con números y colores
    
    Parámetros:
        pantalla: Superficie de Pygame donde dibujar
        estado (dict): Estado actual del juego
        imagen_fondo: Imagen de fondo (puede ser None)
    
    Operación:
        1. Rellena el fondo
        2. Dibuja la imagen de fondo si existe
        3. Dibuja cada celda con su color correspondiente
        4. Dibuja los números en cada celda
        5. Dibuja las líneas del tablero
    """
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar imagen de fondo
    imagen_existe = imagen_fondo is None
    if imagen_existe == False:
        posicion = (0, 0)
        pantalla.blit(imagen_fondo, posicion)
    
    # Obtener datos del estado
    matriz = estado['matriz_juego']
    fijos = estado['matriz_fijos']
    celda_sel = estado['celda_seleccionada']
    estados_celdas = estado.get('estados_celdas', {})
    
    # Dibujar cada celda
    for fila in range(TAMANO_TABLERO):
        for col in range(TAMANO_TABLERO):
            # Calcular posición en píxeles
            x = MARGEN_TABLERO + col * TAMANO_CELDA
            y = MARGEN_TABLERO + fila * TAMANO_CELDA
            
            # Determinar color de fondo de la celda
            color_celda = COLOR_FONDO
            
            celda_es_fija = fijos[fila][col]
            if celda_es_fija:
                color_celda = COLOR_CELDA_FIJA
            else:
                # Verificar si tiene estado de color
                posicion = (fila, col)
                celda_tiene_estado = posicion in estados_celdas
                
                if celda_tiene_estado:
                    tipo = estados_celdas[posicion]
                    
                    if tipo == 'correcto':
                        color_celda = COLOR_CELDA_CORRECTA
                    elif tipo == 'error':
                        color_celda = COLOR_CELDA_ERROR
                    elif tipo == 'duplicado':
                        color_celda = COLOR_CELDA_DUPLICADA
                else:
                    # Verificar si es la celda seleccionada
                    celda_esta_seleccionada = celda_sel is None
                    if celda_esta_seleccionada == False:
                        es_esta_celda = celda_sel == (fila, col)
                        if es_esta_celda:
                            color_celda = COLOR_CELDA_SELECCIONADA
            
            # Dibujar rectángulo de la celda
            rectangulo = (x, y, TAMANO_CELDA, TAMANO_CELDA)
            pygame.draw.rect(pantalla, color_celda, rectangulo)
            
            # Dibujar número si existe
            numero = matriz[fila][col]
            celda_tiene_numero = numero == 0
            
            if celda_tiene_numero == False:
                fuente = pygame.font.Font(None, 40)
                
                # Elegir color del número
                if celda_es_fija:
                    color_numero = COLOR_NUMERO_FIJO
                else:
                    color_numero = COLOR_NUMERO_USUARIO
                
                texto = fuente.render(str(numero), True, color_numero)
                centro_x = x + TAMANO_CELDA // 2
                centro_y = y + TAMANO_CELDA // 2
                centro = (centro_x, centro_y)
                texto_rect = texto.get_rect(center=centro)
                pantalla.blit(texto, texto_rect)
    
    # Dibujar líneas del tablero
    for i in range(TAMANO_TABLERO + 1):
        # Determinar grosor y color de línea
        es_linea_gruesa = i % 3 == 0
        
        if es_linea_gruesa:
            grosor = 3
            color = COLOR_LINEA_GRUESA
        else:
            grosor = 1
            color = COLOR_LINEA
        
        # Línea horizontal
        y = MARGEN_TABLERO + i * TAMANO_CELDA
        inicio_x = MARGEN_TABLERO
        fin_x = MARGEN_TABLERO + TAMANO_TABLERO * TAMANO_CELDA
        inicio = (inicio_x, y)
        fin = (fin_x, y)
        pygame.draw.line(pantalla, color, inicio, fin, grosor)
        
        # Línea vertical
        x = MARGEN_TABLERO + i * TAMANO_CELDA
        inicio_y = MARGEN_TABLERO
        fin_y = MARGEN_TABLERO + TAMANO_TABLERO * TAMANO_CELDA
        inicio = (x, inicio_y)
        fin = (x, fin_y)
        pygame.draw.line(pantalla, color, inicio, fin, grosor)


def dibujar_interfaz(pantalla, estado, botones, imagen_fondo):
    """
    Dibuja la interfaz completa del juego (tablero + información)
    
    Parámetros:
        pantalla: Superficie de Pygame
        estado (dict): Estado actual del juego
        botones (list): Lista de botones a dibujar
        imagen_fondo: Imagen de fondo
    
    Operación:
        1. Dibuja el tablero
        2. Dibuja la información (título, nivel, puntaje)
        3. Dibuja las instrucciones
        4. Dibuja los botones
        5. Dibuja mensaje de victoria si corresponde
    """
    dibujar_tablero(pantalla, estado, imagen_fondo)
    
    # Dibujar información del juego
    fuente_info = pygame.font.Font(None, 30)
    
    # Título
    titulo = fuente_info.render("SUDOKU", True, COLOR_NUMERO_FIJO)
    posicion = (550, 50)
    pantalla.blit(titulo, posicion)
    
    # Nivel
    dificultad = estado['dificultad']
    dificultad_capitalizada = dificultad.capitalize()
    nivel_texto = f"Nivel: {dificultad_capitalizada}"
    nivel = fuente_info.render(nivel_texto, True, COLOR_NUMERO_FIJO)
    posicion = (550, 90)
    pantalla.blit(nivel, posicion)
    
    # Puntaje
    puntaje_actual = estado['puntaje']
    puntaje_texto = f"Puntaje: {puntaje_actual}"
    puntaje = fuente_info.render(puntaje_texto, True, COLOR_NUMERO_FIJO)
    posicion = (550, 130)
    pantalla.blit(puntaje, posicion)
    
    # Instrucciones
    fuente_pequena = pygame.font.Font(None, 20)
    instrucciones = [
        "Controles:",
        "- Click: Seleccionar",
        "- 1-9: Colocar",
        "- Backspace: Borrar",
        "- R: Nuevo tablero",
        "- ESC: Menu"
    ]
    
    y_inicial = 200
    for i in range(len(instrucciones)):
        linea = instrucciones[i]
        texto = fuente_pequena.render(linea, True, COLOR_NUMERO_FIJO)
        y = y_inicial + i * 23
        posicion = (550, y)
        pantalla.blit(texto, posicion)
    
    # Dibujar botones
    for boton in botones:
        dibujar_boton(pantalla, boton)
    
    # Mensaje de victoria
    juego_terminado = estado['juego_terminado']
    if juego_terminado:
        dibujar_mensaje_victoria(pantalla, estado)


def dibujar_boton(pantalla, boton):
    """
    Dibuja un botón con su texto
    
    Parámetros:
        pantalla: Superficie de Pygame
        boton (dict): Diccionario con datos del botón
    
    Operación:
        1. Determina el color según si tiene hover
        2. Dibuja el rectángulo del botón
        3. Dibuja el texto centrado
    """
    # Determinar color
    boton_tiene_colores = 'color' in boton and 'color_hover' in boton
    
    if boton_tiene_colores:
        # Botón con colores personalizados
        mouse_encima = boton.get('hover', False)
        
        if mouse_encima:
            color = boton['color_hover']
        else:
            color = boton['color']
    else:
        # Botón normal
        mouse_encima = boton.get('hover', False)
        
        if mouse_encima:
            color = COLOR_BOTON_HOVER
        else:
            color = COLOR_BOTON
    
    # Dibujar rectángulo
    rectangulo = boton['rect']
    pygame.draw.rect(pantalla, color, rectangulo, border_radius=5)
    
    # Dibujar texto
    fuente = pygame.font.Font(None, 28)
    texto_boton = boton['texto']
    texto = fuente.render(texto_boton, True, COLOR_TEXTO_BOTON)
    centro = rectangulo.center
    texto_rect = texto.get_rect(center=centro)
    pantalla.blit(texto, texto_rect)


def dibujar_mensaje_victoria(pantalla, estado):
    """
    Dibuja el mensaje de victoria cuando se completa el Sudoku
    
    Parámetros:
        pantalla: Superficie de Pygame
        estado (dict): Estado del juego con puntaje final
    
    Operación:
        1. Crea un fondo semi-transparente oscuro
        2. Dibuja mensajes de felicitación y puntaje
    """
    # Fondo semi-transparente
    dimensiones = (ANCHO_VENTANA, ALTO_VENTANA)
    overlay = pygame.Surface(dimensiones)
    overlay.set_alpha(200)
    color_negro = (0, 0, 0)
    overlay.fill(color_negro)
    posicion = (0, 0)
    pantalla.blit(overlay, posicion)
    
    # Mensajes
    fuente_grande = pygame.font.Font(None, 60)
    fuente_mediana = pygame.font.Font(None, 40)
    color_blanco = (255, 255, 255)
    color_gris = (200, 200, 200)
    
    texto1 = fuente_grande.render("¡FELICIDADES!", True, color_blanco)
    
    puntaje_final = estado['puntaje']
    mensaje_puntaje = f"Puntaje Final: {puntaje_final}"
    texto2 = fuente_mediana.render(mensaje_puntaje, True, color_blanco)
    
    texto3 = fuente_mediana.render("Presiona R para jugar de nuevo", True, color_gris)
    
    # Calcular posiciones centradas
    x1 = ANCHO_VENTANA // 2 - texto1.get_width() // 2
    x2 = ANCHO_VENTANA // 2 - texto2.get_width() // 2
    x3 = ANCHO_VENTANA // 2 - texto3.get_width() // 2
    
    pantalla.blit(texto1, (x1, 200))
    pantalla.blit(texto2, (x2, 280))
    pantalla.blit(texto3, (x3, 350))


def crear_botones():
    """
    Crea los botones de la interfaz del juego
    
    Retorna:
        list: Lista de diccionarios con información de cada botón
    """
    botones = [
        {
            'texto': 'Nuevo Juego',
            'rect': pygame.Rect(550, 340, ANCHO_BOTON, ALTO_BOTON),
            'accion': 'nuevo',
            'hover': False
        },
        {
            'texto': 'Reiniciar',
            'rect': pygame.Rect(550, 390, ANCHO_BOTON, ALTO_BOTON),
            'accion': 'reiniciar',
            'hover': False
        },
        {
            'texto': 'Validar',
            'rect': pygame.Rect(550, 440, ANCHO_BOTON, ALTO_BOTON),
            'accion': 'validar',
            'hover': False
        }
    ]
    
    return botones


def obtener_celda_click(pos):
    """
    Convierte coordenadas de click del mouse en posición de celda
    
    Parámetros:
        pos (tuple): Coordenadas (x, y) del click
    
    Operación:
        1. Verifica si el click está dentro del tablero
        2. Calcula la fila y columna correspondiente
    
    Retorna:
        tuple o None: (fila, col) o None si está fuera del tablero
    """
    x = pos[0]
    y = pos[1]
    
    # Calcular límites del tablero
    margen_izquierdo = MARGEN_TABLERO
    margen_derecho = MARGEN_TABLERO + TAMANO_TABLERO * TAMANO_CELDA
    margen_superior = MARGEN_TABLERO
    margen_inferior = MARGEN_TABLERO + TAMANO_TABLERO * TAMANO_CELDA
    
    # Verificar si está dentro del tablero
    esta_fuera_horizontal = x < margen_izquierdo or x > margen_derecho
    esta_fuera_vertical = y < margen_superior or y > margen_inferior
    esta_fuera = esta_fuera_horizontal or esta_fuera_vertical
    
    if esta_fuera:
        return None
    
    # Calcular celda
    col = (x - MARGEN_TABLERO) // TAMANO_CELDA
    fila = (y - MARGEN_TABLERO) // TAMANO_CELDA
    
    return (fila, col)


def actualizar_hover_botones(botones, pos_mouse):
    """
    Actualiza el estado hover de los botones según posición del mouse
    
    Parámetros:
        botones (list): Lista de botones a actualizar
        pos_mouse (tuple): Posición actual del mouse
    
    Operación:
        - Para cada botón, verifica si el mouse está encima
    """
    for boton in botones:
        rectangulo = boton['rect']
        mouse_esta_encima = rectangulo.collidepoint(pos_mouse)
        boton['hover'] = mouse_esta_encima


def obtener_boton_clickeado(botones, pos):
    """
    Determina qué botón fue clickeado
    
    Parámetros:
        botones (list): Lista de botones
        pos (tuple): Posición del click
    
    Operación:
        - Recorre los botones verificando si se clickeó alguno
    
    Retorna:
        str o None: Acción del botón clickeado, o None
    """
    for boton in botones:
        rectangulo = boton['rect']
        fue_clickeado = rectangulo.collidepoint(pos)
        
        if fue_clickeado:
            accion = boton['accion']
            return accion
    
    return None


def dibujar_menu_dificultad(pantalla, imagen_fondo):
    """
    Dibuja el menú de selección de dificultad
    
    Parámetros:
        pantalla: Superficie de Pygame
        imagen_fondo: Imagen de fondo (puede ser None)
    
    Operación:
        1. Dibuja el fondo y la imagen
        2. Dibuja título y subtítulo
        3. Crea y dibuja botones de dificultad
        4. Dibuja información de cada dificultad
    
    Retorna:
        list: Lista de botones de dificultad creados
    """
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar imagen de fondo
    imagen_existe = imagen_fondo is None
    if imagen_existe == False:
        posicion = (0, 0)
        pantalla.blit(imagen_fondo, posicion)
    
    # Título
    fuente_titulo = pygame.font.Font(None, 80)
    titulo = fuente_titulo.render("SUDOKU", True, COLOR_NUMERO_FIJO)
    x = ANCHO_VENTANA // 2 - titulo.get_width() // 2
    pantalla.blit(titulo, (x, 100))
    
    # Subtítulo
    fuente_subtitulo = pygame.font.Font(None, 40)
    subtitulo = fuente_subtitulo.render("Selecciona la dificultad", True, COLOR_NUMERO_FIJO)
    x = ANCHO_VENTANA // 2 - subtitulo.get_width() // 2
    pantalla.blit(subtitulo, (x, 180))
    
    # Crear botones de dificultad
    centro_x = ANCHO_VENTANA // 2
    
    botones = [
        {
            'texto': 'FÁCIL',
            'rect': pygame.Rect(centro_x - 100, 270, 200, 60),
            'accion': 'facil',
            'hover': False,
            'color': COLOR_BOTON_FACIL,
            'color_hover': COLOR_BOTON_FACIL_HOVER
        },
        {
            'texto': 'MEDIO',
            'rect': pygame.Rect(centro_x - 100, 350, 200, 60),
            'accion': 'medio',
            'hover': False,
            'color': COLOR_BOTON_MEDIO,
            'color_hover': COLOR_BOTON_MEDIO_HOVER
        },
        {
            'texto': 'DIFÍCIL',
            'rect': pygame.Rect(centro_x - 100, 430, 200, 60),
            'accion': 'dificil',
            'hover': False,
            'color': COLOR_BOTON_DIFICIL,
            'color_hover': COLOR_BOTON_DIFICIL_HOVER
        }
    ]
    
    # Dibujar botones
    for boton in botones:
        dibujar_boton(pantalla, boton)
    
    # Información adicional
    fuente_info = pygame.font.Font(None, 24)
    color_gris = (100, 100, 100)
    info_lineas = [
        "FÁCIL: 5 números por región",
        "MEDIO: 4 números por región",
        "DIFÍCIL: 3 números por región"
    ]
    
    y_inicial = 520
    for i in range(len(info_lineas)):
        linea = info_lineas[i]
        texto = fuente_info.render(linea, True, color_gris)
        x = ANCHO_VENTANA // 2 - texto.get_width() // 2
        y = y_inicial + i * 30
        pantalla.blit(texto, (x, y))
    
    return botones