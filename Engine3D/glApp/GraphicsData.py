from OpenGL.GL import *
import numpy as np

class GraphicsData():
    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.bufferRef = glGenBuffers(1)
        self.load()
    
    def load(self):
        data = np.array(self.data, np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    def createVariable(self, programId, variableName):
        variableId = glGetAttribLocation(programId, variableName)
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        if self.dataType == "vec2":
            glVertexAttribPointer(variableId, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableId, 3, GL_FLOAT, False, 0, None)
            
        glEnableVertexAttribArray(variableId)