from OpenGL import *
import pygame
from .GraphicsData import *
import numpy as np
from .Uniform import *
from .Transformations import *


class MovingMesh:
    def __init__(self, programId, vertices, vertexColors, drawType, 
                 translation=pygame.Vector3(0, 0, 0),
                 rotation = Rotation(0, pygame.Vector3(0,0,0)), 
                 scale = pygame.Vector3(1,1,1),
                 moveRotation = Rotation(0, pygame.Vector3(0, 1, 0))):
        self.vertices = vertices
        self.drawType = drawType
        
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        position = GraphicsData("vec3", self.vertices)
        position.createVariable(programId, "position")
        colors = GraphicsData("vec3", vertexColors)
        colors.createVariable(programId, "vertexColor")
        
        self.transformationMat = identityMat()
        self.transformationMat = rotateA(self.transformationMat, rotation.angle, rotation.axis)
        self.transformationMat = translate(self.transformationMat, translation.x, translation.y, translation.z)
        self.transformationMat = scale3(self.transformationMat, scale.x, scale.y, scale.z )
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(programId, "modelMat")
        self.moveRotation = moveRotation
        self.programId = programId
        
        
    def draw(self):
        self.transformationMat = rotateA(self.transformationMat, self.moveRotation.angle, self.moveRotation.axis)
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(self.programId, "modelMat")
        self.transformation.load()


        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.vertices))
        
        