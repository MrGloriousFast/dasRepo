from OpenGL.GL import *
from OpenGL.GLU import *
class Particle:
    def __init__(self, pos, speed, direction):
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.tdelta = 0.001

    def update(self):
        self.speed[2] -= self.tdelta * 9.81
        self.pos[0] += self.speed[0] * self.tdelta
        self.pos[1] += self.speed[1] * self.tdelta
        self.pos[2] += self.speed[2] * self.tdelta

    def render(self):
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glVertex3f(*self.pos)
        glEnd();

        #  glVertex2v(*self.pos)

