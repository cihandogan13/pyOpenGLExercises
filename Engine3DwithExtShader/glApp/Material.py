from .Utils import *

class Material:
    def __init__(self, vertexShader, fragmentShader):
        self.programId = createProgram(open(vertexShader).read(),
                                       open(fragmentShader).read())
    
    def use(self):
        glUseProgram(self.programId)
        