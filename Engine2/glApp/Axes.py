from .Mesh import *

class Axes(Mesh):
    def __init__(self, programId, location):
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
        
        super().__init__(programId, vertices, colors, GL_LINES, location)
        
