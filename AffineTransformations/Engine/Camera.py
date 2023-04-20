import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self):
        self.eye   = pygame.math.Vector3(0, 0, 0)
        self.up    = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
        self.yaw = -90
        self.pitch = 0
        self.lastMouse = pygame.math.Vector2(0, 0)
        self.mouseSensitivityX = 0.001
        self.mouseSensitivityY = 0.001
        self.keySensitivity = 0.008
    
    def rotate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch
        
        if self.pitch > 89.0:
            self.pitch = 89.0
            
        if self.pitch < -89.0:
            self.pitch = 89.0
            
        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward.normalize()
        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()
    
    def update(self, width, height):
        if pygame.mouse.get_visible():
            return
        
        mousePos = pygame.mouse.get_pos()
        mouseChange = self.lastMouse - pygame.math.Vector2(mousePos)
        
        pygame.mouse.set_pos(width / 2, height / 2)
        
        self.lastMouse = pygame.mouse.get_pos()
        self.rotate(-mouseChange.x * self.mouseSensitivityX, 
                    mouseChange.y * self.mouseSensitivityY)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * self.keySensitivity
        if keys[pygame.K_UP]:
            self.eye += self.forward * self.keySensitivity
        if keys[pygame.K_LEFT]:
            self.eye -= self.right * self.keySensitivity
        if keys[pygame.K_RIGHT]:
            self.eye += self.right * self.keySensitivity
            
        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
        
        
        