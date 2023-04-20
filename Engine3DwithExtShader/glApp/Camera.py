import pygame
from OpenGL.GLU import *
from math import *
import numpy as np
from .Transformations import *
from .Uniform import *


class Camera:
    def __init__(self, width, height):
        self.transformation = identityMat()
        self.lastMouse = pygame.math.Vector2(0, 0)
        self.mouseSensitivityX = 0.1
        self.mouseSensitivityY = 0.1
        self.keySensitivity = 0.08
        self.projectionMat = self.perspectiveMat(60, width/height, 0.01, 10000)
        self.projection = Uniform("mat4", self.projectionMat)
        
        self.screenWidth = width
        self.screenHeight = height
        
    
    
    def perspectiveMat(self, angleOfView, aspectRatio, nearPlane, farPlane):
        angle = radians(angleOfView)
        d = 1.0/tan(angle/2.0)
        ratio = aspectRatio
        b = (farPlane + nearPlane) / (nearPlane - farPlane)
        c = farPlane * nearPlane / (nearPlane - farPlane)
        #transpose of perspective matrix
        return np.array([[d/ratio, 0,  0, 0 ],
                         [      0, d,  0, 0 ],
                         [      0, 0,  b, c ],
                         [      0, 0, -1, 0 ]], np.float32)
        
    
    def rotate(self, yaw, pitch):
        forward = pygame.Vector3(self.transformation[0,2], self.transformation[1,2], self.transformation[2,2])
        up = pygame.Vector3(0, 1, 0)
        angle = forward.angle_to(up)
        
        self.transformation = rotate(self.transformation, yaw, "Y", False)
        if angle < 170.0 and pitch > 0  or angle > 30.0 and pitch < 0:
            self.transformation = rotate(self.transformation, pitch, "X", True)
        
    
    def update(self, programId):
        if pygame.mouse.get_visible():
            return
        
        mousePos = pygame.mouse.get_pos()
        mouseChange = self.lastMouse - pygame.math.Vector2(mousePos)
        
        pygame.mouse.set_pos(self.screenWidth / 2, self.screenHeight / 2)
        
        self.lastMouse = pygame.mouse.get_pos()
        self.rotate(mouseChange.x * self.mouseSensitivityX, 
                    mouseChange.y * self.mouseSensitivityY)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.transformation = translate(self.transformation, 0, 0, self.keySensitivity)
        if keys[pygame.K_UP]:
            self.transformation = translate(self.transformation, 0, 0, -self.keySensitivity)
        if keys[pygame.K_LEFT]:
            self.transformation = translate(self.transformation, -self.keySensitivity, 0, 0)
        if keys[pygame.K_RIGHT]:
            self.transformation = translate(self.transformation, self.keySensitivity, 0, 0)
        
        
        self.projection.findVariable(programId, "projectionMat")
        self.projection.load()
        lookAtMat = self.transformation 
        lookAt = Uniform("mat4", lookAtMat)
        lookAt.findVariable(programId, "viewMat")
        lookAt.load()
        
        
        