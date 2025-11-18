# Example file showing a basic pygame "game loop"
import pygame as pg
import pygame.mixer as mixer

# pygame setup
pg.init()
mixer.init()

evento_tick = pg.USEREVENT + 1
tiempo_ms = 1000

mixer.music.load("./intro_stage.mp3")
mixer.music.set_volume(0.02)
#mixer.music.play()

sonido = mixer.Sound("./megaman_shoot.mp3")
sonido.set_volume(0.4)

ALTO_VENTANA = 720
ANCHO_VENTANA = 1280

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#clock = pg.time.Clock()
running = True
descuento_tiempo = 20
x = 300
y = 300
coordenadas = (x, y, 100, 100)
imagen = pg.image.load("megaman.png")
megaman = imagen.get_rect()
megaman.x = x
megaman.y = y
y1 = y/2
x1 = x/2
#otro_rectangulo = pg.draw.rect(screen, (255, 0, 0), pg.Rect(100, 100, 50, 50))
#circulo = pg.draw.circle(screen, (255, 0, 0), (x, y), 70.6)
texto_ingresado = "TEXTO"


imagen_vertical = pg.Surface((x, y))
imagen_vertical.fill((255,0,0))
rectangulo = imagen_vertical.get_rect()
rectangulo.x = (ANCHO_VENTANA - rectangulo.width) // 2
rectangulo.y = (ALTO_VENTANA - rectangulo.height) // 2

pg.time.set_timer(evento_tick, tiempo_ms)
#mega = pg.Surface.get_rect(imagen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                
                megaman.x -= 10
            if event.key == pg.K_RIGHT:
                megaman.x += 10

            if event.key == pg.K_UP:
                megaman.y -= 10

            if event.key == pg.K_DOWN:
                megaman.y += 10

            
            #Entrada de teclado
            if event.key == pg.K_SPACE:
                texto_ingresado = texto_ingresado[0:-1]
                x = input('INGRESA TEXTO: ')
                print(texto_ingresado)
            elif event.key == pg.K_RETURN:
                print("PRESIONASTE ENTER")
                
                print(x)
            else: 
                texto_ingresado += event.unicode
                print(texto_ingresado)

        if event.type == pg.MOUSEBUTTONUP:
            posicion = (event.pos)
            if event.button == 1:  # Left mouse button
                print('SOLTASTE EL BOTON IZQUIERDO')
                megaman.x = posicion[0]
                megaman.y = posicion[1] 
            if event.button == 3:  # Right mouse button
                print('SOLTASTE EL BOTON DERECHO')    
        if event.type == pg.MOUSEBUTTONDOWN:
            posicion = (event.pos)
            if event.button == 1:  # Left mouse button
                print('PRESIONASTE EL BOTON IZQUIERDO')
            if event.button == 3:  # Right mouse button
                print('PRESIONASTE EL BOTON DERECHO')
            

        if event.type ==  evento_tick: 
            megaman.x += 10
            #print(f'ES UN RELOJ {descuento_tiempo}')
                
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        megaman.x -= 10
    if keys[pg.K_RIGHT]:
        megaman.x += 10
    if keys[pg.K_UP]:
        megaman.y -= 10
    if keys[pg.K_DOWN]:
        megaman.y += 10

    """
    if megaman.x > 350 and megaman.x < 800:
        
        mixer.music.pause()
        sonido.play()   
    elif megaman.x >= 900 :
        
        sonido.stop()
    else:
        mixer.music.unpause()
    """                 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0,104,100))

    #DIBUJAR IMAGEN
    #screen.blit(cuadro, (x, y))
    
    #100 ANCHO RECT 20 ALTO
    #centrar = ((ANCHO_VENTANA/2,ALTO_VENTANA/2))
    screen.blit(imagen_vertical, rectangulo)
    screen.blit(imagen, megaman)

    
       
    
    #screen.blit(otro_rectangulo, (400,400))
   
    #cuadro = pg.draw.rect(screen, ('blue'), coordenadas, 115,5,5,5)
    
    
    
    #screen.blit(cuadro, (x,y))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.update()
    pg.display.flip()
    

    