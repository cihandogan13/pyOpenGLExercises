from glApp.PyOGLApp import *


class RefactorTest(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        
    def initialise(self):
        background_color = (0, 0, 0, 1)
        drawing_color = (1, 1, 1, 1)
        glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
        glColor(drawing_color)

        # projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.screenWidth / self.screenHeight), 0.1, 100.0) 
        

         # modelview
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, self.screenWidth, self.screenHeight)
        glEnable(GL_DEPTH_TEST)
        self.camera.update(self.screenWidth, self.screenHeight)
        
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.drawWorldAxes()
        
RefactorTest().mainLoop()
