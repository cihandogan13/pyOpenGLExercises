from pygame.locals import *
from .Camera import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *


class PyOGLApp():
    def __init__(self, screenPosX, screenPosY, screenWidth, screenHeight):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screenPosX,screenPosY)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1) #anti alias
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4) #anti alias
        #for opengl-pygame vertex shader MUST HAVE
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)     
        self.screen = pygame.display.set_mode((screenWidth, screenWidth), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('OpenGL in Python')
        self.camera = None
        self.programId = None
        self.clock = pygame.time.Clock()
        
    def drawWorldAxes(self):
        glLineWidth(4)
        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3d(-1000, 0, 0)
        glVertex3d(1000, 0, 0)
        
        glColor3f(0, 1, 0)
        glVertex3d(0, 1000, 0)
        glVertex3d(0, -1000, 0)
        
        glColor3f(0, 0, 1)
        glVertex3d(0, 0, 1000)
        glVertex3d(0, 0, -1000)
        glEnd()
        glLineWidth(1)
        
        sphere = gluNewQuadric()
        
        #x pos sphere
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
        
        glLineWidth(1)
        glColor(1,1,1)
        
    def initialise(self):
        pass
    
    def display(self):
        pass
    
    def cameraInit(self):
        pass
    
    def mainLoop(self):
        done = False
        self.initialise()
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
            self.cameraInit()
            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
 