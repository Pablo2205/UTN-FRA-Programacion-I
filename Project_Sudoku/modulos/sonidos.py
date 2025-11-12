"""
================================================================================
MÓDULO: sonidos.py
DESCRIPCIÓN: Gestiona la música de fondo y los efectos de sonido del juego
             Carga, reproduce y controla todos los sonidos
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
import pygame
import os
from modulos.configuracion import *


# -------------------- FUNCIONES --------------------
def inicializar_sonidos():
    """
    Inicializa el sistema de sonido de Pygame
    
    Operación:
        - Inicializa el mixer de Pygame para reproducir audio
    """
    pygame.mixer.init()


def cargar_musica_fondo():
    """
    Carga y reproduce la música de fondo en loop infinito
    
    Operación:
        1. Verifica si existe el archivo de música
        2. Carga la música
        3. Establece el volumen configurado
        4. Reproduce en loop infinito
    
    Retorna:
        bool: True si se cargó correctamente, False si hubo error
    """
    archivo_existe = os.path.exists(RUTA_MUSICA_FONDO)
    
    if archivo_existe == False:
        mensaje = f"Advertencia: No se encontró el archivo de música '{RUTA_MUSICA_FONDO}'"
        print(mensaje)
        return False
    
    pygame.mixer.music.load(RUTA_MUSICA_FONDO)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)  # -1 significa loop infinito
    
    return True


def detener_musica():
    """
    Detiene la música de fondo completamente
    """
    pygame.mixer.music.stop()


def pausar_musica():
    """
    Pausa la música de fondo (puede reanudarse después)
    """
    pygame.mixer.music.pause()


def reanudar_musica():
    """
    Reanuda la música de fondo si estaba pausada
    """
    pygame.mixer.music.unpause()


def cargar_efectos_sonido():
    """
    Carga todos los efectos de sonido del juego
    
    Operación:
        1. Crea diccionario vacío para efectos
        2. Define rutas de todos los sonidos
        3. Intenta cargar cada sonido
        4. Establece volumen configurado
    
    Retorna:
        dict: Diccionario con todos los efectos cargados
              Las claves son: inicio, reiniciar, validar, correcto, error, victoria
    """
    efectos = {
        'inicio': None,
        'reiniciar': None,
        'validar': None,
        'correcto': None,
        'error': None,
        'victoria': None
    }
    
    rutas = {
        'inicio': RUTA_SONIDO_INICIO,
        'reiniciar': RUTA_SONIDO_REINICIAR,
        'validar': RUTA_SONIDO_VALIDAR,
        'correcto': RUTA_SONIDO_CORRECTO,
        'error': RUTA_SONIDO_ERROR,
        'victoria': RUTA_SONIDO_VICTORIA
    }
    
    # Cargar cada efecto de sonido
    for nombre in rutas:
        ruta = rutas[nombre]
        archivo_existe = os.path.exists(ruta)
        
        if archivo_existe:
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(VOLUMEN_EFECTOS)
            efectos[nombre] = sonido
        else:
            mensaje = f"Advertencia: No se encontró el archivo de sonido '{ruta}'"
            print(mensaje)
    
    return efectos


def reproducir_sonido(efectos, nombre):
    """
    Reproduce un efecto de sonido específico
    
    Parámetros:
        efectos (dict): Diccionario con todos los efectos cargados
        nombre (str): Nombre del efecto a reproducir
    
    Operación:
        1. Busca el efecto en el diccionario
        2. Si existe, lo reproduce
    """
    efecto_existe = efectos.get(nombre) is None
    
    if efecto_existe == False:
        sonido = efectos[nombre]
        sonido.play()


def ajustar_volumen_musica(volumen):
    """
    Ajusta el volumen de la música de fondo
    
    Parámetros:
        volumen (float): Volumen entre 0.0 (silencio) y 1.0 (máximo)
    
    Operación:
        - Limita el volumen entre 0.0 y 1.0
        - Aplica el nuevo volumen a la música
    """
    # Limitar volumen entre 0.0 y 1.0
    if volumen < 0.0:
        volumen_ajustado = 0.0
    elif volumen > 1.0:
        volumen_ajustado = 1.0
    else:
        volumen_ajustado = volumen
    
    pygame.mixer.music.set_volume(volumen_ajustado)


def ajustar_volumen_efectos(efectos, volumen):
    """
    Ajusta el volumen de todos los efectos de sonido
    
    Parámetros:
        efectos (dict): Diccionario con todos los efectos
        volumen (float): Volumen entre 0.0 y 1.0
    
    Operación:
        - Limita el volumen entre 0.0 y 1.0
        - Aplica el nuevo volumen a cada efecto
    """
    # Limitar volumen entre 0.0 y 1.0
    if volumen < 0.0:
        volumen_ajustado = 0.0
    elif volumen > 1.0:
        volumen_ajustado = 1.0
    else:
        volumen_ajustado = volumen
    
    # Aplicar a todos los efectos
    for nombre in efectos:
        efecto = efectos[nombre]
        efecto_existe = efecto is None
        
        if efecto_existe == False:
            efecto.set_volume(volumen_ajustado)