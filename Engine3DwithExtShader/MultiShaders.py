import numpy as np
from OpenGL.arrays.vbo import VBO
from glApp.PyOGLApp import *
from glApp.LoadMesh import *
from glApp.Light import *
from glApp.Material import *
from glApp.Axes import *




class MultiShaders(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.floor=None
        self.tabletop = None
        self.teapot = None
        self.leg1 = None
        self.leg2 = None
        self.leg3 = None
        self.leg4 = None
        self.lights = []
        self.axes = None
        glEnable(GL_CULL_FACE)
        
    def initialise(self):
        projectPath = "/home/ubuntu/Projects/CourseMaterials/Engine3DwithExtShader/"
        mat = Material(projectPath + "shaders/texturedvert.glsl",
                       projectPath + "shaders/texturedfrag.glsl")
        
        axesMat = Material(projectPath + "shaders/vertexcolvert.glsl",
                       projectPath + "shaders/vertexcolfrag.glsl")

        self.axes = Axes(pygame.Vector3(0, 0, 0), axesMat)
        self.floor = LoadMesh(projectPath + "models/plane.obj",
                              projectPath + "images/tiles.png",
                              location=pygame.Vector3(0, -1.5, 0),
                              scale=pygame.Vector3(5, 1, 5),
                              material=mat)
        self.tabletop = LoadMesh(projectPath + "models/tabletop.obj",
                             projectPath + "images/timber.png",
                             location=pygame.Vector3(0, -0.5, 0),
                             scale=pygame.Vector3(1.2, 0.8, 1.2),
                             material=mat)
        self.teapot = LoadMesh(projectPath + "models/teapot.obj",
                             projectPath + "images/gold.png",
                             location=pygame.Vector3(0.5, -0.5, 0),
                             scale=pygame.Vector3(0.2, 0.2, 0.2),
                             material=mat)

        self.leg1 = LoadMesh(projectPath + "models/tableleg.obj",
                             projectPath + "images/timber.png",
                             location=pygame.Vector3(-0.5, -1, 0.5),
                             scale=pygame.Vector3(1.2, 0.8, 1.2),
                             material=mat)
        self.leg2 = LoadMesh(projectPath + "models/tableleg.obj",
                             projectPath + "images/timber.png",
                             location=pygame.Vector3(-0.5, -1, -0.5),
                             scale=pygame.Vector3(1.2, 0.8, 1.2),
                             material=mat)
        self.leg3 = LoadMesh(projectPath + "models/tableleg.obj",
                             projectPath + "images/timber.png",
                             location=pygame.Vector3(0.5, -1, -0.5),
                             scale=pygame.Vector3(1.2, 0.8, 1.2),
                             material=mat)
        self.leg4 = LoadMesh(projectPath + "models/tableleg.obj",
                             projectPath + "images/timber.png",
                             location=pygame.Vector3(0.5, -1, 0.5),
                             scale=pygame.Vector3(1.2, 0.8, 1.2),
                             material=mat)



        self.lights.append(Light(pygame.Vector3(0, 1, 0), pygame.Vector3(1, 1, 1), 0))
        #self.lights.append(Light(pygame.Vector3(1, 1, 0), pygame.Vector3(1, 1, 1), 1))
        self.camera = Camera(self.screenWidth, self.screenHeight)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def cameraInit(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # self.camera.update()
        # self.light.update()
        self.axes.draw(self.camera, None)
        self.tabletop.draw(self.camera, self.lights)
        self.leg1.draw(self.camera, self.lights)
        self.leg2.draw(self.camera, self.lights)
        self.leg3.draw(self.camera, self.lights)
        self.leg4.draw(self.camera, self.lights)
        self.floor.draw(self.camera, self.lights)
        self.teapot.draw(self.camera, self.lights)

MultiShaders().mainLoop()