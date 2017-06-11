
import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
from obj import *
from display import *
from camera import *
from manager import *


class Group():
    def __init__(self, shader, mesh, texture):
        self.bodies = []
        self.shader = shader
        self.texture = texture
        self.mesh = mesh
        
    def insert(self, body):
        self.bodies.append(body)
        self.mesh.extend(body.verticies, body.texcords, body.indicies)
        
    def updateShader(self, cam):
        v = cam.view()
        p = cam.projection()
        for b in self.bodies:
            #print(b.posWorld.get())
            self.shader.update(b.posWorld.get(), v, p)
        
    def updateBodies(self, deltaT):
        counter = 0
        for b in self.bodies:
            b.update(deltaT, counter)
            counter += 1
            
    def draw(self):

        self.shader.use()
        self.texture.bind()
        self.mesh.draw()
