from glApp.PyOGLApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO
from glApp.GraphicsData import *
from glApp.Square import *
from glApp.Triangle import *


vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertexColor;
uniform vec3 translation;
out vec3 color;
void main()
{
    vec3 pos  = position + translation;
    gl_Position = vec4(pos, 1);
    color = vertexColor;
}
'''

fragment_shader = r'''
#version 330 core
out vec4 fragColor;
in vec3 color;
void main()
{
    fragColor = vec4(color, 1);
}
'''

class ShaderTest(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.vao_ref = None
        self.vertexCount = 0
        self.square = None
        self.triangle = None
        
    def initialise(self):
        self.programId = createProgram(vertex_shader, fragment_shader)
        #self.vao_ref = glGenVertexArrays(1)
        #glBindVertexArray(self.vao_ref)
        #glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        #glPointSize(10)
        
        # positionData = [[0, -0.9, 0],
        #                  [-0.6, 0.8, 0],
        #                  [0.9, -0.2, 0],
        #                  [-0.9, -0.2, 0],
        #                  [0.6, 0.8, 0]]
        # self.vertexCount = len(positionData)
        # positionVariable = GraphicsData("vec3", positionData)
        # positionVariable.createVariable(self.programId, "position")
        
        # colorData = [[1, 0, 0],
        #              [0, 1, 0],
        #              [0, 0, 1],
        #              [1, 0, 1],
        #              [1, 1, 0]]
        # colorVariable = GraphicsData("vec3", colorData)
        # colorVariable.createVariable(self.programId, "vertexColor")
        self.square = Square(self.programId, pygame.Vector3(-1, 1, 0))
        self.triangle = Triangle(self.programId, pygame.Vector3(0.5, -0.5, 0))
        

    def cameraInit(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programId)
        #glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        self.square.draw()
        self. triangle.draw()

ShaderTest().mainLoop()