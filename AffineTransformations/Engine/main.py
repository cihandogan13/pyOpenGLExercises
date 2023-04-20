import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *
from Camera import *
import os


x = 850
y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
#mesh = Mesh()
cube = Cube(GL_LINE_LOOP, position=pygame.Vector3(2,0,0), rotation = Rotation(45, pygame.Vector3(0,1,0)), scale=pygame.Vector3(0.5, 0.5, 0.5))
cube2 = Cube(GL_LINE_LOOP, position=pygame.Vector3(2,0,0), rotation = Rotation(45, pygame.Vector3(0,1,0)))
mesh = LoadMesh("CourseMaterials/AffineTransformations/Engine/objFiles/donut.obj",GL_LINE_LOOP)
camera = Camera()

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0) #granny 100.0->1000.0

def initCamera():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update(screen.get_width(), screen.get_height())


def drawWorldAxes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3f(0.75, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)
    
    glColor3f(0, 0.75, 0)
    glVertex3d(0, 1000, 0)
    glVertex3d(0, -1000, 0)
    
    glColor3f(0, 0, 0.75)
    glVertex3d(0, 0, 1000)
    glVertex3d(0, 0, -1000)
    glEnd()
    glLineWidth(1)
    
    #x pos sphere
    sphere = gluNewQuadric()
    glColor(1,0,0)
    glPushMatrix()
    glTranslated(1,0,0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()
    
    #y 
    glColor(0,1,0)
    glPushMatrix()
    glTranslated(0,1,0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()
    
    #z
    glColor(0,0,1)
    glPushMatrix()
    glTranslated(0,0,1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()
    


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    initCamera()
    drawWorldAxes()
    glColor3f(0.7, 0.7, 0.7)
    glRotated(45,0,0,1)
    cube.draw()
    #glScale(0.5, 0.5, 0.5)
    cube2.draw()
    


done = False
initialise()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
            if event.key == K_SPACE:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)
    display()
    pygame.display.flip()
    #pygame.time.wait(100)
pygame.quit()