from copy import deepcopy
from OpenGL.GL import *
from OpenGL.GLU import *
from Physical import Physical

class Particle(Physical):
    def __init__(self, pos, speed, direction, die_after):
        self.pos = deepcopy(pos)
        self.speed = deepcopy(speed)
        self.direction = deepcopy(direction)
        self.tdelta = 0.08

    def update(self):
        self.speed[2] -= self.tdelta * 0.5
        self.pos[0] += self.speed[0] * self.tdelta
        self.pos[1] += self.speed[1] * self.tdelta
        self.pos[2] += self.speed[2] * self.tdelta

    def render(self):
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glVertex3f(*self.pos)
        glEnd();

