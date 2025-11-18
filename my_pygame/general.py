'''
import pygame
pygame.init()  

# Set up the display
size = (800, 600)
screen = pygame.display.set_mode(size)
  
# Main loop
while True:  
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

'''