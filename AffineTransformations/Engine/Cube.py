from OpenGL.GL import *
from Mesh import *
import pygame




class Cube(Mesh):
    def __init__(self, drawType, position = pygame.math.Vector3(0, 0 , 0), rotation = Rotation(0, pygame.Vector3(0,0,0)), scale = pygame.Vector3(1,1,1)):
        vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, -0.5, -0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (-0.5, 0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, 0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (0.5, -0.5, 0.5)]
        triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]
        #self.drawType = drawType
        super().__init__(vertices, triangles, drawType, position, rotation, scale)