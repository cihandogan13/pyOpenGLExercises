from .Mesh import *

class Square(Mesh):
    def __init__(self, programId, location):
        vertices = [[0.5, 0.5, -1.0],
                    [0.5, -0.5, -1.0],
                    [-0.5, -0.5, -1.0],
                    [-0.5, 0.5, -1.0]]
        colors = [[1, 0, 0],
                  [1, 0.5, 0],
                  [1, 1, 0],
                  [0, 1, 0]]
        super().__init__(programId, vertices, colors, GL_TRIANGLE_FAN, location)