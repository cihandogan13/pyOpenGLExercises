import numpy as np
from math import *

def identityMat():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)

def translateMat(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]], np.float32)

def scaleMat(scale):
    return np.array([[scale,     0,     0, 0],
                     [    0, scale,     0, 0],
                     [    0,     0, scale, 0],
                     [    0,     0,     0, 1]], np.float32)
    
def scaleMat3(scaleX, scaleY, scaleZ):
    return np.array([[scaleX,      0,      0, 0],
                     [     0, scaleY,      0, 0],
                     [     0,      0, scaleZ, 0],
                     [     0,      0,      0, 1]], np.float32)
    
def rotateXMat(angle):
    ang = radians(angle)
    cosAng = cos(ang)
    sinAng = sin(ang)
    return np.array([[1,      0,       0, 0],
                     [0, cosAng, -sinAng, 0],
                     [0, sinAng,  cosAng, 0],
                     [0,      0,       0, 1]], np.float32)

def rotateYMat(angle):
    ang = radians(angle)
    cosAng = cos(ang)
    sinAng = sin(ang)
    return np.array([[ cosAng, 0, sinAng, 0],
                     [      0, 1,      0, 0],
                     [-sinAng, 0, cosAng, 0],
                     [      0, 0,      0, 1]], np.float32)

def rotateZMat(angle):
    ang = radians(angle)
    cosAng = cos(ang)
    sinAng = sin(ang)
    return np.array([[cosAng, -sinAng, 0, 0],
                     [sinAng,  cosAng, 0, 0], 
                     [     0,       0, 1, 0],
                     [     0,       0, 0, 1]], np.float32)
    
def translate(matrix, x, y, z):
    transMatrix = translateMat(x, y, z)
    return matrix @ transMatrix

def scale(matrix, scale):
    scaleMatrix = scaleMat(scale)
    return matrix @ scaleMatrix

def scale3(matrix, scaleX, scaleY ,scaleZ):
    scaleMatrix = scaleMat3(scaleX, scaleY, scaleZ)
    return matrix @ scaleMatrix

def rotate(matrix, angle, axis, local = True):
    rotationMatrix = identityMat()
    if axis == "X":
        rotationMatrix = rotateXMat(angle)
    elif axis == "Y":
        rotationMatrix = rotateYMat(angle)
    elif axis == "Z":
        rotationMatrix = rotateZMat(angle)   
    if local:     
        return matrix @ rotationMatrix
    else:
        return rotationMatrix @ matrix        


     
    
    