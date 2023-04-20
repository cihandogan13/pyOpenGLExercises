from OpenGL import *
import pygame
from .GraphicsData import *
import numpy as np
from .Uniform import *
from .Transformations import *


class Mesh:
    def __init__(self, programId, vertices, vertexColors, drawType, translation=pygame.Vector3(0, 0, 0)):
        self.vertices = vertices
        self.drawType = drawType
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        position = GraphicsData("vec3", self.vertices)
        position.createVariable(programId, "position")
        colors = GraphicsData("vec3", vertexColors)
        colors.createVariable(programId, "vertexColor")
        self.transformationMat = identityMat()
        self.transformationMat = translate(self.transformationMat, translation.x, translation.y, translation.z)
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(programId, "modelMat")
        
        
    def draw(self):
        self.transformation.load()
        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.vertices))
        
        