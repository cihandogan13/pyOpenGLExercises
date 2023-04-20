from OpenGL import *
import pygame
import numpy as np
from .GraphicsData import *
from .Uniform import *
from .Transformations import *
from .Texture import *



class Mesh:
    def __init__(self, programId, vertices, imagefile, vertexNormals, vertexUVs, vertexColors, drawType, 
                 translation=pygame.Vector3(0, 0, 0),
                 rotation = Rotation(0, pygame.Vector3(0,0,0)), 
                 scale = pygame.Vector3(1,1,1),
                 moveRotation = Rotation(0, pygame.Vector3(0, 1, 0)),
                 moveTranslate=pygame.Vector3(0, 0, 0),
                 moveScale = pygame.Vector3(1,1,1)):
        
        self.vertices = vertices
        self.vertexNormals = vertexNormals
        self.vertexUVs = vertexUVs
        self.drawType = drawType
        
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        position = GraphicsData("vec3", self.vertices)
        position.createVariable(programId, "position")
        colors = GraphicsData("vec3", vertexColors)
        colors.createVariable(programId, "vertexColor")
        normals = GraphicsData("vec3", vertexNormals)
        normals.createVariable(programId, "vertexNormal")
        uvs = GraphicsData("vec2", vertexUVs)
        uvs.createVariable(programId, "vertexUV")
        
        self.transformationMat = identityMat()
        self.transformationMat = rotateA(self.transformationMat, rotation.angle, rotation.axis)
        self.transformationMat = translate(self.transformationMat, translation.x, translation.y, translation.z)
        self.transformationMat = scale3(self.transformationMat, scale.x, scale.y, scale.z )
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(programId, "modelMat")
        self.moveRotation = moveRotation
        self.moveTranslate = moveTranslate
        self.moveScale = moveScale
        self.programId = programId
        self.image = Texture(imagefile)
        self.texture = Uniform("sampler2D",[self.image.textureId, 1])
        self.texture.findVariable(programId, "tex")

        
        
    def draw(self):
        self.texture.load()
        self.transformationMat = rotateA(self.transformationMat, self.moveRotation.angle, self.moveRotation.axis)
        self.transformationMat = translate(self.transformationMat, self.moveTranslate.x, self.moveTranslate.y, self.moveTranslate.z)
        self.transformationMat = scale3(self.transformationMat, self.moveScale.x, self.moveScale.y, self.moveScale.z )
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(self.programId, "modelMat")
        self.transformation.load()


        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.vertices))
        
        