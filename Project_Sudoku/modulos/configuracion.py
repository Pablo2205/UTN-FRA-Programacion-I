"""
================================================================================
MÓDULO: configuracion.py
DESCRIPCIÓN: Contiene todas las constantes y configuraciones del juego Sudoku
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# ==================== CONFIGURACIÓN DE VENTANA ====================
ANCHO_VENTANA = 800  # Ancho de la ventana en píxeles
ALTO_VENTANA = 600   # Alto de la ventana en píxeles
TITULO = "Sudoku - UTN Avellaneda"  # Título que aparece en la ventana
FPS = 30  # Frames por segundo del juego

# ==================== ESTADOS DEL JUEGO ====================
ESTADO_MENU = 'menu'  # Menú principal
ESTADO_USUARIOS = 'usuarios'  # Pantalla de selección de usuario
ESTADO_DIFICULTAD = 'dificultad'  # Selector de dificultad
ESTADO_JUGANDO = 'jugando'  # Jugando partida
ESTADO_PUNTAJES = 'puntajes'  # Visualización de puntajes
ESTADO_CREAR_USUARIO = 'crear_usuario'  # Input para crear usuario

# ==================== CONFIGURACIÓN DEL TABLERO ====================
TAMANO_TABLERO = 9  # Tamaño del tablero Sudoku (9x9)
TAMANO_CELDA = 50   # Tamaño de cada celda en píxeles
MARGEN_TABLERO = 50  # Margen desde el borde de la ventana

# ==================== RUTAS DE RECURSOS ====================
# Ruta de la imagen de fondo (logo UTN)
RUTA_IMAGEN_FONDO = "assets/imagenes/logo_utn.png"
OPACIDAD_FONDO = 30  # Opacidad del logo (0=invisible, 255=opaco)

# Rutas de archivos de sonido
RUTA_MUSICA_FONDO = "assets/sonidos/musica_fondo.mp3"
RUTA_SONIDO_INICIO = "assets/sonidos/inicio.wav"
RUTA_SONIDO_REINICIAR = "assets/sonidos/reiniciar.wav"
RUTA_SONIDO_VALIDAR = "assets/sonidos/validar.wav"
RUTA_SONIDO_CORRECTO = "assets/sonidos/correcto.wav"
RUTA_SONIDO_ERROR = "assets/sonidos/error.wav"
RUTA_SONIDO_VICTORIA = "assets/sonidos/victoria.wav"

# ==================== CONFIGURACIÓN DE AUDIO ====================
VOLUMEN_MUSICA = 0.3   # Volumen de la música de fondo (0.0 a 1.0)
VOLUMEN_EFECTOS = 0.5  # Volumen de los efectos de sonido (0.0 a 1.0)

# ==================== COLORES RGB ====================
# Colores generales
COLOR_FONDO = (240, 240, 240)  # Fondo de la ventana
COLOR_LINEA = (0, 0, 0)  # Líneas delgadas del tablero
COLOR_LINEA_GRUESA = (0, 0, 0)  # Líneas gruesas (cada 3 celdas)

# Colores de números
COLOR_NUMERO_FIJO = (0, 0, 0)  # Números del sistema (negros)
COLOR_NUMERO_USUARIO = (0, 100, 200)  # Números del jugador (azules)

# Colores de celdas
COLOR_CELDA_SELECCIONADA = (200, 220, 255)  # Celda seleccionada (azul claro)
COLOR_CELDA_FIJA = (200, 200, 200)  # Números fijos del sistema (gris)
COLOR_CELDA_CORRECTA = (200, 255, 200)  # Número correcto (verde)
COLOR_CELDA_DUPLICADA = (255, 255, 150)  # Número duplicado (amarillo)
COLOR_CELDA_ERROR = (255, 200, 200)  # Número incorrecto (rojo)

# Colores de botones generales
COLOR_BOTON = (100, 150, 200)  # Color normal del botón
COLOR_BOTON_HOVER = (120, 170, 220)  # Color cuando el mouse pasa por encima
COLOR_TEXTO_BOTON = (255, 255, 255)  # Color del texto del botón (blanco)

# Colores de botones de dificultad (Flat UI Design)
COLOR_BOTON_FACIL = (26, 188, 156)  # Verde azulado
COLOR_BOTON_FACIL_HOVER = (22, 160, 133)  # Verde azulado oscuro
COLOR_BOTON_MEDIO = (230, 126, 34)  # Naranja cálido
COLOR_BOTON_MEDIO_HOVER = (211, 84, 0)  # Naranja vibrante
COLOR_BOTON_DIFICIL = (231, 76, 60)  # Rojo coral
COLOR_BOTON_DIFICIL_HOVER = (192, 57, 43)  # Rojo coral oscuro

# ==================== CONFIGURACIÓN DE DIFICULTAD ====================
# Cantidad de números iniciales por región (3x3) según dificultad
DIFICULTAD = {
    'facil': 5,    # 5 números visibles por región
    'medio': 4,    # 4 números visibles por región
    'dificil': 3   # 3 números visibles por región
}

# ==================== CONFIGURACIÓN DE PUNTUACIÓN ====================
PUNTAJE_INICIAL = 0  # Puntos al comenzar el juego
DESCUENTO_POR_ERROR = 1  # Puntos que se restan por número incorrecto
PUNTOS_ZONA_COMPLETA = 9  # Puntos al completar una fila/columna/región
PUNTOS_COMPLETAR_TABLERO = 81  # Puntos extra al completar todo el tablero

# ==================== CONFIGURACIÓN DE BOTONES ====================
ALTO_BOTON = 40  # Alto de los botones en píxeles
ANCHO_BOTON = 150  # Ancho de los botones en píxeles
MARGEN_BOTON = 10  # Margen entre botones

# Botones del menú principal
ALTO_BOTON_MENU = 50
ANCHO_BOTON_MENU = 200

# ==================== CONFIGURACIÓN DE INPUT DE TEXTO ====================
ANCHO_INPUT = 300  # Ancho del campo de texto
ALTO_INPUT = 40  # Alto del campo de texto
COLOR_INPUT_FONDO = (255, 255, 255)  # Blanco
COLOR_INPUT_BORDE = (100, 100, 100)  # Gris
COLOR_INPUT_TEXTO = (0, 0, 0)  # Negro
COLOR_INPUT_ACTIVO = (100, 150, 200)  # Azul cuando está activo

# ==================== CONFIGURACIÓN DE TABLA DE PUNTAJES ====================
COLOR_ENCABEZADO_TABLA = (50, 50, 50)  # Gris oscuro
COLOR_FILA_PAR = (240, 240, 240)  # Gris claro
COLOR_FILA_IMPAR = (255, 255, 255)  # Blanco
COLOR_TEXTO_TABLA = (0, 0, 0)  # Negro
ALTO_FILA_TABLA = 35  # Alto de cada fila