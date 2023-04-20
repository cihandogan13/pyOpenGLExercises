from .Mesh import *

class Axes(Mesh):
    def __init__(self, location, material):
        
        vertices = [[-100,    0,    0],
                    [ 100,    0,    0],
                    [   0, -100,    0],
                    [   0,  100,    0],
                    [   0,    0, -100],
                    [   0,    0,  100]]
        
        colors = [[1, 0, 0],
                  [1, 0, 0],
                  [0, 1, 0],
                  [0, 1, 0], 
                  [0, 0, 1],
                  [0, 0, 1]]
        
        super().__init__(vertices, 
                         vertexColors=colors, 
                         drawType=GL_LINES, 
                         translation=location,
                         material=material)
        