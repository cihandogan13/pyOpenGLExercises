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

class MovingObjects(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.axes = None
        self.movingCube = None
        self.teapot=None
        self.movingTeapot=None
        
    def initialise(self):
        self.programId = createProgram(vertex_shader, fragment_shader)
        self.axes = Axes(self.programId, pygame.Vector3(0.0, 0.0, 0.0))
        self.movingCube = Cube(self.programId,
                                     location=pygame.Vector3(2, 1, 2),
                                     moveRotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        teapot = "CourseMaterials/Engine3D/models/teapot.obj"
        self.teapot = LoadMesh(teapot, self.programId,
                               moveTranslate=pygame.Vector3(0.1, 0, 0),
                               moveRotation=Rotation(2, pygame.Vector3(1, 1, 0)))
        self.movingTeapot = LoadMesh(teapot, self.programId, 
                                location=pygame.Vector3(2, -2, 2),
                                moveRotation=Rotation(2, pygame.Vector3(1, 1, 0)))
        self.camera = Camera(self.programId, self.screenWidth, self.screenHeight)
        glEnable(GL_DEPTH_TEST)

    def cameraInit(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programId)
        self.camera.update()
        self.axes.draw()
        self.movingCube.draw()
        self.teapot.draw()
        self.movingTeapot.draw()

MovingObjects().mainLoop()