from OpenGL.GL import *
import pygame

class Rotation:
    def __init__(self, angle, axis):
        self.angle = angle
        self.axis = axis


class Mesh:
    def __init__(self, vertices, triangles, drawType, translation, rotation, scale):
        self.vertices = vertices
        self.triangles = triangles
        self.drawType = drawType
        self.translation = translation
        self.rotation = rotation
        self.scale = scale
        
    def draw(self, move = pygame.math.Vector3(0, 0, 0)):
        glPushMatrix()
        glTranslatef(move.x, move.y, move.z)
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)
        glScalef(self.scale.x, self.scale.y, self.scale.z) #scale affects translate but rotation so it matters AFTER translate
        glRotatef(self.rotation.angle, self.rotation.axis.x, self.rotation.axis.y, self.rotation.axis.z)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.drawType)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glPopMatrix()
            