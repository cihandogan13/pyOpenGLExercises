import pygame

from .Transformations import *
from .Uniform import *

class Light:
    def __init__(self,programId, position= pygame.Vector3(0,0,0), color=pygame.Vector3(1,1,1), lightNumber=0,):
        self.transformation = identityMat()
        self.programId = programId
        self.position = position
        self.color = color
        self.lightVariable = "lightData[" + str(lightNumber) + "].position"
        self.colorVariable = "lightData[" + str(lightNumber) + "].color"

    def update(self):
        lightPosition = Uniform("vec3", self.position)
        lightPosition.findVariable(self.programId, self.lightVariable)
        lightPosition.load()
        color = Uniform("vec3", self.color)
        color.findVariable(self.programId, self.colorVariable)
        color.load()