from OpenGL.GL import *
import numpy as np

def formatVertices(coordinates, triangles):
    allTriangles = []
    for t in range(0, len(triangles), 3):
        allTriangles.append(coordinates[triangles[t]])
        allTriangles.append(coordinates[triangles[t+1]])
        allTriangles.append(coordinates[triangles[t+2]])
    return np.array(allTriangles, np.float32)


def compileShader(shaderType, shaderSource):
    shaderId = glCreateShader(shaderType)
    glShaderSource(shaderId, shaderSource)
    glCompileShader(shaderId)
    compileSuccess = glGetShaderiv(shaderId, GL_COMPILE_STATUS)
    if not compileSuccess:
        errorMessage = glGetShaderInfoLog(shaderId)
        glDeleteShader(shaderId)
        errorMessage = "\n" + errorMessage.decode("utf-8")
        raise Exception(errorMessage)
    return shaderId

def createProgram(vertexShaderCode, fragmentShaderCode):
    vertexShaderId = compileShader(GL_VERTEX_SHADER, vertexShaderCode)
    fragmentShaderId = compileShader(GL_FRAGMENT_SHADER, fragmentShaderCode)
    programId = glCreateProgram()
    glAttachShader(programId, vertexShaderId)
    glAttachShader(programId, fragmentShaderId)
    glLinkProgram(programId)
    linkSuccess = glGetProgramiv(programId, GL_LINK_STATUS)
    if not linkSuccess:
        info = glGetProgramInfoLog(programId)
        raise RuntimeError(info)
    glDeleteShader(vertexShaderId)
    glDeleteShader(fragmentShaderId)
    return programId

