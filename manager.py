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
        self.mesh.insert(body.verticies, body.texcords)
        
    #same as above but for many at once
    def insertAll(self, bodies):
        self.bodies.extend(bodies)
        v=[]
        t=[]


        for body in bodies:
            v.extend(body.verticies)
            t.extend(body.texcords)

        self.mesh.insert(v,t)
        
        
    def updateShader(self, cam):
        self.shader.use()
        self.shader.updateCam(cam)


    def updateBodies(self, deltaT):
        counter = 0
        for b in self.bodies:
            b.update(deltaT, counter)
            counter += 1

            
    def draw(self):
        self.shader.use()
        self.texture.bind()
        self.mesh.bind()

        for b in self.bodies:
            self.shader.updatePos(b.posWorld.get())
            b.mesh.render()






