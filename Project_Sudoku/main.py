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

from modulos.configuracion import FPS
from modulos.logica import (inicializar_juego, seleccionar_celda, colocar_numero, 
                             borrar_numero, reiniciar_juego)
from modulos.validacion import validar_solucion
from modulos.interfaz import (inicializar_pygame, dibujar_interfaz, crear_botones,
                               obtener_celda_click, actualizar_hover_botones, 
                               obtener_boton_clickeado, dibujar_menu_dificultad)
from modulos.sonidos import (inicializar_sonidos, cargar_musica_fondo, cargar_efectos_sonido,
                              reproducir_sonido)

#454545454545
# -------------------- FUNCIÓN PRINCIPAL --------------------
def main():
    """
    Función principal que ejecuta el juego
    
    Operación:
        1. Inicializa Pygame y carga recursos
        2. Entra en el bucle principal del juego
        3. Maneja eventos del usuario (clicks, teclas)
        4. Actualiza la pantalla constantemente
        5. Controla el flujo entre menú y juego
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
    
    # Variables de estado del juego
    en_menu = True
    estado = None
    botones_menu = None
    botones = crear_botones()
    
    # Variable para mensajes temporales
    mensaje_temporal = {
        'texto': '',
        'tiempo': 0
    }
    
    # ===== BUCLE PRINCIPAL =====
    ejecutando = True
    while ejecutando:
        
        # ===== MANEJO DE EVENTOS =====
        for evento in pygame.event.get():
            
            # ----- Evento: Cerrar ventana -----
            tipo_evento_es_quit = evento.type == QUIT
            if tipo_evento_es_quit:
                ejecutando = False
            
            # ----- Evento: Click del mouse -----
            tipo_evento_es_click = evento.type == MOUSEBUTTONDOWN
            if tipo_evento_es_click:
                boton_izquierdo = evento.button == 1
                
                if boton_izquierdo:
                    pos = pygame.mouse.get_pos()
                    
                    # --- Si estamos en el menú de dificultad ---
                    if en_menu:
                        menu_existe = botones_menu is None
                        
                        if menu_existe == False:
                            accion = obtener_boton_clickeado(botones_menu, pos)
                            es_dificultad = accion in ['facil', 'medio', 'dificil']
                            
                            if es_dificultad:
                                # Iniciar juego con dificultad seleccionada
                                estado = inicializar_juego(accion)
                                en_menu = False
                                reproducir_sonido(efectos_sonido, 'inicio')
                    
                    # --- Si estamos jugando ---
                    else:
                        # Verificar si se clickeó un botón
                        accion = obtener_boton_clickeado(botones, pos)
                        
                        # Botón "Nuevo Juego" - volver al menú
                        if accion == 'nuevo':
                            en_menu = True
                            mensaje_temporal['texto'] = ''
                            mensaje_temporal['tiempo'] = 0
                        
                        # Botón "Reiniciar" - nuevo tablero misma dificultad
                        elif accion == 'reiniciar':
                            dificultad_actual = estado['dificultad']
                            estado = inicializar_juego(dificultad_actual)
                            mensaje_temporal['texto'] = 'Nuevo tablero generado'
                            mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                            reproducir_sonido(efectos_sonido, 'reiniciar')
                        
                        # Botón "Validar" - verificar solución
                        elif accion == 'validar':
                            resultado = validar_solucion(estado)
                            reproducir_sonido(efectos_sonido, 'validar')
                            
                            solucion_correcta = resultado['correcta']
                            if solucion_correcta:
                                mensaje_temporal['texto'] = 'Solucion completa!'
                                mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                            else:
                                # Construir mensaje con estadísticas
                                partes = []
                                
                                correctas = resultado['total_correctas']
                                if correctas > 0:
                                    parte = f"OK: {correctas}"
                                    partes.append(parte)
                                
                                incorrectas = resultado['total_incorrectas']
                                if incorrectas > 0:
                                    parte = f"Error: {incorrectas}"
                                    partes.append(parte)
                                
                                vacias = resultado['total_vacias']
                                if vacias > 0:
                                    parte = f"Vacias: {vacias}"
                                    partes.append(parte)
                                
                                hay_partes = len(partes) > 0
                                if hay_partes:
                                    texto = " | ".join(partes)
                                else:
                                    texto = "Sin numeros"
                                
                                mensaje_temporal['texto'] = texto
                                mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                        
                        # No se clickeó botón - verificar si se clickeó celda
                        else:
                            celda = obtener_celda_click(pos)
                            celda_existe = celda is None
                            
                            if celda_existe == False:
                                fila = celda[0]
                                col = celda[1]
                                seleccionar_celda(estado, fila, col)
            
            # ----- Evento: Tecla presionada -----
            tipo_evento_es_tecla = evento.type == KEYDOWN
            estamos_jugando = en_menu == False
            
            if tipo_evento_es_tecla and estamos_jugando:
                
                # Tecla ESC - volver al menú
                if evento.key == K_ESCAPE:
                    en_menu = True
                    mensaje_temporal['texto'] = ''
                    mensaje_temporal['tiempo'] = 0
                
                # Tecla R - reiniciar con misma dificultad
                elif evento.key == K_r:
                    dificultad_actual = estado['dificultad']
                    estado = inicializar_juego(dificultad_actual)
                    mensaje_temporal['texto'] = 'Nuevo tablero generado'
                    mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                    reproducir_sonido(efectos_sonido, 'reiniciar')
                
                # Teclas 1-9 - colocar número
                elif K_1 <= evento.key <= K_9:
                    numero = evento.key - K_0
                    resultado = colocar_numero(estado, numero)
                    
                    mensaje_temporal['texto'] = resultado['mensaje']
                    mensaje_temporal['tiempo'] = pygame.time.get_ticks()
                    
                    # Reproducir sonido según resultado
                    tipo = resultado['tipo']
                    
                    if tipo == 'correcto':
                        reproducir_sonido(efectos_sonido, 'correcto')
                        
                        # Si ganó el juego
                        juego_terminado = estado['juego_terminado']
                        if juego_terminado:
                            reproducir_sonido(efectos_sonido, 'victoria')
                    
                    elif tipo == 'error':
                        reproducir_sonido(efectos_sonido, 'error')
                
                # Tecla Backspace o Delete - borrar número
                elif evento.key == K_BACKSPACE or evento.key == K_DELETE:
                    se_borro = borrar_numero(estado)
                    
                    if se_borro:
                        mensaje_temporal['texto'] = 'Número borrado'
                        mensaje_temporal['tiempo'] = pygame.time.get_ticks()
        
        # ===== ACTUALIZACIÓN =====
        pos_mouse = pygame.mouse.get_pos()
        
        # ===== DIBUJO =====
        if en_menu:
            # Dibujar menú de selección de dificultad
            botones_menu = dibujar_menu_dificultad(pantalla, imagen_fondo)
            actualizar_hover_botones(botones_menu, pos_mouse)
        else:
            # Actualizar hover de botones del juego
            actualizar_hover_botones(botones, pos_mouse)
            
            # Dibujar interfaz del juego
            dibujar_interfaz(pantalla, estado, botones, imagen_fondo)
            
            # Mostrar mensaje temporal (durante 2 segundos)
            hay_mensaje = mensaje_temporal['texto'] == ''
            
            if hay_mensaje == False:
                tiempo_actual = pygame.time.get_ticks()
                tiempo_mensaje = mensaje_temporal['tiempo']
                diferencia = tiempo_actual - tiempo_mensaje
                mensaje_visible = diferencia < 2000
                
                if mensaje_visible:
                    fuente = pygame.font.Font(None, 24)
                    color_verde = (0, 100, 0)
                    texto_render = mensaje_temporal['texto']
                    texto = fuente.render(texto_render, True, color_verde)
                    posicion = (550, 500)
                    pantalla.blit(texto, posicion)
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