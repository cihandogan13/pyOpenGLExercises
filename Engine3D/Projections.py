import numpy as np
from OpenGL.arrays.vbo import VBO
from glApp.PyOGLApp import *
from glApp.Utils import *
from glApp.GraphicsData import *
from glApp.Square import *
from glApp.Triangle import *
from glApp.Axes import *
from glApp.Cube import *
from glApp.LoadMesh import *

vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertexColor;
uniform mat4 projectionMat;
uniform mat4 modelMat;
uniform mat4 viewMat;
out vec3 color;
void main()
{
    
    gl_Position = projectionMat * inverse(viewMat) * modelMat * vec4(position, 1.0);
    color = vertexColor;
}
'''

fragment_shader = r'''
#version 330 core
out vec4 fragColor;
in vec3 color;
void main()
{
    fragColor = vec4(color, 1.0f);
}
'''

class Projections(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        #self.vao_ref = None
        #self.vertexCount = 0
        self.square = None
        self.triangle = None
        self.axes = None
        self.cube = None
        self.teapot = None
        
    def initialise(self):
        self.programId = createProgram(vertex_shader, fragment_shader)
        #self.square = Square(self.programId, pygame.Vector3(-0.5, 0.5, 0.0))
        #self.triangle = Triangle(self.programId, pygame.Vector3(0.5, -0.5, 0.0))
        self.axes = Axes(self.programId, pygame.Vector3(0.0, 0.0, 0.0))
        #self.cube = Cube(self.programId)
        self.teapot = LoadMesh("CourseMaterials/Engine3D/models/teapot.obj", self.programId, 
                               scale=pygame.Vector3(5, 10, 5),
                               rotation=Rotation(45, pygame.Vector3(1, 0, 1)))
        self.camera = Camera(self.programId, self.screenWidth, self.screenHeight)
        glEnable(GL_DEPTH_TEST)

    def cameraInit(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programId)
        self.camera.update()
        #self.square.draw()
        #self.triangle.draw()
        self.axes.draw()
        #self.cube.draw()
        self.teapot.draw()

Projections().mainLoop()