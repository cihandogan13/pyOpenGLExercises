from .Mesh import *
from .Utils import *
import numpy as np


class Cube(Mesh):
    def __init__(self, programId, location=pygame.Vector3(0, 0, 0), 
                 moveRotation=Rotation(0,pygame.Vector3(0,1,0)),
                 moveTranslate=pygame.Vector3(0, 0, 0),
                 moveScale = pygame.Vector3(1,1,1)):
        coordinates = [(0.5, -0.5, 0.5),
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
        
        colors = np.random.uniform(low=0.0, high=1.0, size=(36,3))
        vertices = formatVertices(coordinates, triangles)
        super().__init__(programId, vertices, colors, GL_TRIANGLES, location, moveRotation=moveRotation, moveTranslate=moveTranslate, moveScale=moveScale)