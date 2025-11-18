"""
================================================================================
PROGRAMA: main.py
DESCRIPCIÓN: Programa principal del juego Sudoku
             Controla el bucle principal y maneja todos los eventos
AUTOR: UTN Avellaneda - Tecnicatura Universitaria en Programación
FECHA: 2024
================================================================================
"""

# -------------------- IMPORTS --------------------
import pygame
from pygame.locals import *
import sys

from modulos.configuracion import *
from modulos.logica import (inicializar_juego, seleccionar_celda, colocar_numero, 
                             borrar_numero, reiniciar_juego, validar_y_calcular_puntaje)
from modulos.validacion import validar_solucion
from modulos.interfaz import *
from modulos.sonidos import *
from modulos.usuarios import *


# -------------------- FUNCIÓN PRINCIPAL --------------------
def main():
    """
    Función principal que ejecuta el juego
    
    Operación:
        1. Inicializa Pygame y carga recursos
        2. Maneja estados del juego (menú, usuarios, jugando, etc.)
        3. Procesa eventos y actualiza pantalla
    """
    # ===== INICIALIZACIÓN =====
    resultado_pygame = inicializar_pygame()
    pantalla = resultado_pygame[0]
    reloj = resultado_pygame[1]
    imagen_fondo = resultado_pygame[2]
    
    # Inicializar sistema de sonidos
    inicializar_sonidos()
    cargar_musica_fondo()
    efectos_sonido = cargar_efectos_sonido()
    
    # ===== VARIABLES DE ESTADO =====
    estado_juego = ESTADO_MENU
    estado_sudoku = None
    usuario_actual = ""
    dificultad_seleccionada = "medio"
    botones = []
    
    # Para input de texto
    texto_input = ""
    input_activo = False
    
    # Para mensajes temporales
    mensaje_temporal = {'texto': '', 'tiempo': 0}
    
    # Tiempo de inicio de partida
    tiempo_inicio = 0
    
    # ===== BUCLE PRINCIPAL =====
    ejecutando = True
    while ejecutando:
        
        # ===== MANEJO DE EVENTOS =====
        for evento in pygame.event.get():
            
            # ----- Evento: Cerrar ventana -----
            if evento.type == QUIT:
                ejecutando = False
            
            # ----- Evento: Click del mouse -----
            elif evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pos = pygame.mouse.get_pos()
                    accion = obtener_boton_clickeado(botones, pos)
                    
                    # ===== MENÚ PRINCIPAL =====
                    if estado_juego == ESTADO_MENU:
                        if accion == 'nivel':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_DIFICULTAD
                        
                        elif accion == 'jugar':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_USUARIOS
                        
                        elif accion == 'puntajes':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_PUNTAJES
                        
                        elif accion == 'salir':
                            reproducir_sonido(efectos_sonido, 'click')
                            ejecutando = False
                    
                    # ===== SELECTOR DE DIFICULTAD =====
                    elif estado_juego == ESTADO_DIFICULTAD:
                        if accion in ['facil', 'medio', 'dificil']:
                            dificultad_seleccionada = accion
                            mensaje_temporal['texto'] = f'Dificultad: {accion.capitalize()}'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                            estado_juego = ESTADO_MENU
                    
                    # ===== PANTALLA DE USUARIOS =====
                    elif estado_juego == ESTADO_USUARIOS:
                        if accion == 'crear':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_CREAR_USUARIO
                            texto_input = ""
                            input_activo = True
                        
                        elif accion == 'volver':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_MENU
                        
                        elif accion and accion.startswith('usuario_'):
                            indice = int(accion.split('_')[1])
                            reproducir_sonido(efectos_sonido, 'click')
                            usuarios = obtener_usuarios()
                            usuario_actual = usuarios[indice]
                            
                            # Iniciar juego
                            estado_sudoku = inicializar_juego(dificultad_seleccionada, usuario_actual)
                            tiempo_inicio = pygame.time.get_ticks()
                            estado_juego = ESTADO_JUGANDO
                            reproducir_sonido(efectos_sonido, 'inicio')
                    
                    # ===== CREAR USUARIO =====
                    elif estado_juego == ESTADO_CREAR_USUARIO:
                        if accion == 'confirmar':
                            reproducir_sonido(efectos_sonido, 'click')
                            resultado = crear_usuario(texto_input)
                            
                            if resultado['exito']:
                                usuario_actual = texto_input
                                estado_sudoku = inicializar_juego(dificultad_seleccionada, usuario_actual)
                                tiempo_inicio = pygame.time.get_ticks()
                                estado_juego = ESTADO_JUGANDO
                                reproducir_sonido(efectos_sonido, 'inicio')
                            else:
                                mensaje_temporal['texto'] = resultado['mensaje']
                                mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                        
                        elif accion == 'cancelar':
                            reproducir_sonido(efectos_sonido, 'click')
                            estado_juego = ESTADO_USUARIOS
                            texto_input = ""
                    
                    # ===== JUGANDO =====
                    elif estado_juego == ESTADO_JUGANDO:
                        if accion == 'nuevo':
                            # Guardar partida si está incompleta
                            if estado_sudoku['juego_terminado'] == False:
                                tiempo_jugado = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                                guardar_partida(usuario_actual, estado_sudoku['puntaje'], 
                                              dificultad_seleccionada, tiempo_jugado)
                            
                            estado_juego = ESTADO_MENU
                            estado_sudoku = None
                        
                        elif accion == 'reiniciar':
                            estado_sudoku = inicializar_juego(dificultad_seleccionada, usuario_actual)
                            tiempo_inicio = pygame.time.get_ticks()
                            reproducir_sonido(efectos_sonido, 'reiniciar')
                            mensaje_temporal['texto'] = 'Nuevo tablero generado'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                        
                        elif accion == 'validar':
                            resultado = validar_y_calcular_puntaje(estado_sudoku)
                            reproducir_sonido(efectos_sonido, 'validar')
                            
                            # Construir mensaje
                            if resultado['completo']:
                                mensaje = 'Sudoku completo!'
                                
                                # Guardar partida exitosa
                                tiempo_jugado = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                                guardar_partida(usuario_actual, resultado['puntaje_final'],
                                              dificultad_seleccionada, tiempo_jugado)
                                reproducir_sonido(efectos_sonido, 'victoria')
                            else:
                                partes = []
                                if resultado['correctas'] > 0:
                                    partes.append(f"OK: {resultado['correctas']}")
                                if resultado['incorrectas'] > 0:
                                    partes.append(f"Error: {resultado['incorrectas']}")
                                if resultado['vacias'] > 0:
                                    partes.append(f"Vacias: {resultado['vacias']}")
                                
                                if len(partes) > 0:
                                    mensaje = " | ".join(partes) + f" | Pts: {resultado['puntaje_final']}"
                                else:
                                    mensaje = "Sin numeros"
                            
                            mensaje_temporal['texto'] = mensaje
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                        
                        else:
                            # Click en celda del tablero
                            celda = obtener_celda_click(pos)
                            if celda:
                                seleccionar_celda(estado_sudoku, celda[0], celda[1])
                    
                    # ===== PUNTAJES =====
                    elif estado_juego == ESTADO_PUNTAJES:
                        if accion == 'volver':
                            estado_juego = ESTADO_MENU
                        
                        elif accion == 'descargar_txt':
                            reproducir_sonido(efectos_sonido, 'click')
                            exportar_puntajes_txt()
                            mensaje_temporal['texto'] = 'Descargado: puntajes.txt'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                        
                        elif accion == 'descargar_csv':
                            reproducir_sonido(efectos_sonido, 'click')
                            exportar_puntajes_csv()
                            mensaje_temporal['texto'] = 'Descargado: puntajes.csv'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
            
            # ----- Evento: Teclas -----
            elif evento.type == KEYDOWN:
                
                # Input de texto (crear usuario)
                if estado_juego == ESTADO_CREAR_USUARIO and input_activo:
                    if evento.key == K_RETURN:
                        # Confirmar creación
                        reproducir_sonido(efectos_sonido, 'click')
                        resultado = crear_usuario(texto_input)
                        
                        if resultado['exito']:
                            usuario_actual = texto_input
                            estado_sudoku = inicializar_juego(dificultad_seleccionada, usuario_actual)
                            tiempo_inicio = pygame.time.get_ticks()
                            estado_juego = ESTADO_JUGANDO
                            reproducir_sonido(efectos_sonido, 'inicio')
                        else:
                            mensaje_temporal['texto'] = resultado['mensaje']
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                    
                    elif evento.key == K_BACKSPACE:
                        texto_input = texto_input[:-1]
                    
                    elif evento.key == K_ESCAPE:
                        estado_juego = ESTADO_USUARIOS
                        texto_input = ""
                    
                    else:
                        # Agregar carácter
                        if len(texto_input) < 20:
                            texto_input = texto_input + evento.unicode
                
                # Teclas durante el juego
                elif estado_juego == ESTADO_JUGANDO:
                    if evento.key == K_ESCAPE:
                        # Guardar partida
                        if estado_sudoku['juego_terminado'] == False:
                            tiempo_jugado = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                            guardar_partida(usuario_actual, estado_sudoku['puntaje'],
                                          dificultad_seleccionada, tiempo_jugado)
                        
                        estado_juego = ESTADO_MENU
                        estado_sudoku = None
                    
                    elif evento.key == K_r:
                        estado_sudoku = inicializar_juego(dificultad_seleccionada, usuario_actual)
                        tiempo_inicio = pygame.time.get_ticks()
                        reproducir_sonido(efectos_sonido, 'reiniciar')
                    
                    elif K_1 <= evento.key <= K_9:
                        numero = evento.key - K_0
                        resultado = colocar_numero(estado_sudoku, numero)
                        mensaje_temporal['texto'] = resultado['mensaje']
                        mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                    
                    elif evento.key == K_BACKSPACE or evento.key == K_DELETE:
                        if borrar_numero(estado_sudoku):
                            mensaje_temporal['texto'] = 'Número borrado'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
        
        # ===== ACTUALIZACIÓN =====
        pos_mouse = pygame.mouse.get_pos()
        if len(botones) > 0:
            actualizar_hover_botones(botones, pos_mouse)
        
        # ===== DIBUJO =====
        if estado_juego == ESTADO_MENU:
            botones = dibujar_menu_principal(pantalla, imagen_fondo)
            
            # Mostrar mensaje temporal
            if mensaje_temporal['texto']:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - mensaje_temporal['tiempo'] < 2000:
                    fuente = pygame.font.Font(None, 24)
                    texto = fuente.render(mensaje_temporal['texto'], True, (0, 100, 0))
                    x = ANCHO_VENTANA // 2 - texto.get_width() // 2
                    pantalla.blit(texto, (x, 550))
                else:
                    mensaje_temporal['texto'] = ''
        
        elif estado_juego == ESTADO_DIFICULTAD:
            botones = dibujar_menu_dificultad(pantalla, imagen_fondo)
        
        elif estado_juego == ESTADO_USUARIOS:
            usuarios = obtener_usuarios()
            botones = dibujar_pantalla_usuarios(pantalla, usuarios, imagen_fondo)
        
        elif estado_juego == ESTADO_CREAR_USUARIO:
            resultado_input = dibujar_input_nombre(pantalla, texto_input, input_activo, imagen_fondo)
            botones = resultado_input['botones']
            
            # Mostrar mensaje temporal
            if mensaje_temporal['texto']:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - mensaje_temporal['tiempo'] < 3000:
                    fuente = pygame.font.Font(None, 24)
                    texto = fuente.render(mensaje_temporal['texto'], True, (200, 0, 0))
                    x = ANCHO_VENTANA // 2 - texto.get_width() // 2
                    pantalla.blit(texto, (x, 400))
                else:
                    mensaje_temporal['texto'] = ''
        
        elif estado_juego == ESTADO_JUGANDO:
            botones = crear_botones()
            dibujar_interfaz(pantalla, estado_sudoku, botones, imagen_fondo)
            
            # Mostrar mensaje temporal
            if mensaje_temporal['texto']:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - mensaje_temporal['tiempo'] < 2000:
                    fuente = pygame.font.Font(None, 22)
                    texto = fuente.render(mensaje_temporal['texto'], True, (0, 100, 0))
                    pantalla.blit(texto, (550, 500))
                else:
                    mensaje_temporal['texto'] = ''
        
        elif estado_juego == ESTADO_PUNTAJES:
            puntajes = obtener_top_puntajes(5)
            botones = dibujar_pantalla_puntajes(pantalla, puntajes, imagen_fondo)
            
            # Mostrar mensaje temporal
            if mensaje_temporal['texto']:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - mensaje_temporal['tiempo'] < 2000:
                    fuente = pygame.font.Font(None, 24)
                    texto = fuente.render(mensaje_temporal['texto'], True, (0, 100, 0))
                    x = ANCHO_VENTANA // 2 - texto.get_width() // 2
                    pantalla.blit(texto, (x, 440))
                else:
                    mensaje_temporal['texto'] = ''
        
        # ===== ACTUALIZAR PANTALLA =====
        pygame.display.flip()
        reloj.tick(FPS)
    
    # ===== FINALIZACIÓN =====
    pygame.quit()
    sys.exit()


# -------------------- EJECUCIÓN --------------------
main()