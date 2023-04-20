from OpenGL.GL import *
from .Mesh import *
from .Utils import *
import pygame
import random

class LoadMesh(Mesh):
    def __init__(self, filename, imagefile, 
                 drawType=GL_TRIANGLES, 
                 location = pygame.Vector3(0, 0 , 0),
                 rotation = Rotation(0, pygame.Vector3(0,0,0)), 
                 scale = pygame.Vector3(1,1,1),
                 moveRotation = Rotation(0, pygame.Vector3(0, 1, 0)),
                 moveTranslate=pygame.Vector3(0, 0, 0),
                 moveScale = pygame.Vector3(1,1,1),
                 material=None ):
        coordinates, triangles, uvs, uvIndices, normals, normalIndices = self.loadDrawing(filename)
        vertices = formatVertices(coordinates, triangles)
        vertexNormals = formatVertices(normals, normalIndices)
        vertexUVs = formatVertices(uvs, uvIndices)
        colors = []
        for index in range(len(vertices)):
            colors.append(1)
            colors.append(1)
            colors.append(1)
        super().__init__(vertices, 
                         imagefile=imagefile,
                         vertexNormals=vertexNormals,
                         vertexUVs=vertexUVs,
                         vertexColors=colors, 
                         drawType=drawType, 
                         translation=location, 
                         rotation=rotation, 
                         scale=scale, 
                         moveRotation=moveRotation, 
                         moveTranslate=moveTranslate, 
                         moveScale=moveScale,
                         material=material)
        
    def loadDrawing(self, filename):
        vertices = []
        triangles = []

        normals = []
        normalIndices = []

        uvValues = []
        uvIndices=[]
        with open(filename) as fp:
            line= fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "vn":
                    normalX, normalY, normalZ = [float(value) for value in line[3:].split()]
                    normals.append((normalX, normalY, normalZ))
                if line[:2] == "vt":
                    uvX, uvY = [float(value) for value in line[3:].split()]
                    uvValues.append((uvX, uvY))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)

                    uvIndices.append([int(value) for value in t1.split('/')][1]-1)
                    uvIndices.append([int(value) for value in t2.split('/')][1]-1)
                    uvIndices.append([int(value) for value in t3.split('/')][1]-1)

                    normalIndices.append([int(value) for value in t1.split('/')][2]-1)
                    normalIndices.append([int(value) for value in t2.split('/')][2]-1)
                    normalIndices.append([int(value) for value in t3.split('/')][2]-1)
                line = fp.readline()
                
        return vertices, triangles, uvValues, uvIndices, normals, normalIndices