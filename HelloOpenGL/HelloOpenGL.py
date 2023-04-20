import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()


screenWidth =1000
screenHeight =800

screen = pygame.display.set_mode((screenWidth,screenHeight), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def initOrtho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,640,0,480)



done = False
initOrtho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(100,50)
    glVertex2i(630,450)
    glEnd()
    
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()