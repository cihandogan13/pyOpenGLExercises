from OpenGL import *
import pygame
import numpy as np
from .GraphicsData import *
from .Uniform import *
from .Transformations import *
from .Texture import *



class Mesh:
    def __init__(self, vertices, 
                 imagefile=None,
                 vertexNormals=None, 
                 vertexUVs=None,
                 vertexColors=None,
                 drawType=GL_TRIANGLES, 
                 translation=pygame.Vector3(0, 0, 0),
                 rotation = Rotation(0, pygame.Vector3(0,0,0)), 
                 scale = pygame.Vector3(1,1,1),
                 moveRotation = Rotation(0, pygame.Vector3(0, 1, 0)),
                 moveTranslate=pygame.Vector3(0, 0, 0),
                 moveScale = pygame.Vector3(1,1,1),
                 material=None ):
        
        self.material=material
        self.vertices = vertices
        self.vertexNormals = vertexNormals
        self.vertexUVs = vertexUVs
        self.drawType = drawType
        
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        if vertices is not None: 
            position = GraphicsData("vec3", self.vertices)
            position.createVariable(self.material.programId, "position")

        if vertexColors is not None: 
            colors = GraphicsData("vec3", vertexColors)
            colors.createVariable(self.material.programId, "vertexColor")

        if vertexNormals is not None:
            normals = GraphicsData("vec3", vertexNormals)
            normals.createVariable(self.material.programId, "vertexNormal")

        if vertexUVs is not None:    
            uvs = GraphicsData("vec2", vertexUVs)
            uvs.createVariable(self.material.programId, "vertexUV")
        
        self.transformationMat = identityMat()
        self.transformationMat = rotateA(self.transformationMat, rotation.angle, rotation.axis)
        self.transformationMat = translate(self.transformationMat, translation.x, translation.y, translation.z)
        self.transformationMat = scale3(self.transformationMat, scale.x, scale.y, scale.z )
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(self.material.programId, "modelMat")
        self.moveRotation = moveRotation
        self.moveTranslate = moveTranslate
        self.moveScale = moveScale
        self.texture = None
        if imagefile is not None: 
            self.image = Texture(imagefile)
            self.texture = Uniform("sampler2D",[self.image.textureId, 1])

        
        
    def draw(self, camera, lights):
        self.material.use()
        camera.update(self.material.programId)
        if lights is not None:
            for light in lights:
                light.update(self.material.programId)

        if self.texture is not None: 
            self.texture.findVariable(self.material.programId, "tex")
            self.texture.load()

        self.transformationMat = rotateA(self.transformationMat, self.moveRotation.angle, self.moveRotation.axis)
        self.transformationMat = translate(self.transformationMat, self.moveTranslate.x, self.moveTranslate.y, self.moveTranslate.z)
        self.transformationMat = scale3(self.transformationMat, self.moveScale.x, self.moveScale.y, self.moveScale.z )
        self.transformation = Uniform("mat4", self.transformationMat)
        self.transformation.findVariable(self.material.programId, "modelMat")
        self.transformation.load()


        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.vertices))
        
        