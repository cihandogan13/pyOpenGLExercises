from OpenGL.GL import *

class Uniform():
    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.variableId = None
    
    def findVariable(self, programId, variableName):
        self.variableId = glGetUniformLocation(programId, variableName)
        
    def load(self):
        if self.dataType == "vec3":
            glUniform3f(self.variableId, self.data[0],self.data[1],self.data[2])
        elif self.dataType == "mat4":
            glUniformMatrix4fv(self.variableId, 1, GL_TRUE, self.data)
        elif self.dataType == "sampler2D":
            textureObj, textureUnit = self.data
            glActiveTexture(GL_TEXTURE0 + textureUnit)
            glBindTexture(GL_TEXTURE_2D, textureObj)
            glUniform1i(self.variableId, textureUnit)
            
            
        