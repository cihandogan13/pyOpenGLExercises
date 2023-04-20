import pygame
from pygame.locals import *

pygame.init()


screenWidth =1000
screenHeight =800

screen = pygame.display.set_mode((screenWidth,screenHeight), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()