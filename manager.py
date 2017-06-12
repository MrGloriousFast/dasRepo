
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
        print("orig:")
        print(body.posWorld.get())
        print()
        t =[]
        for i in body.posWorld.get():
            t.extend(i)

        self.mesh.extend(body.verticies, body.texcords, t, body.indicies)
        
        
    def extend(self, bodies):
        self.bodies.extend(bodies)
        v=[]
        t=[]
        i=[]
        p=[]


        for body in bodies:
            v.extend(body.verticies)
            t.extend(body.texcords)
            i.extend(body.indicies)
            p.extend(body.posWorld.get())
            
        self.mesh.extend(v,t,p,i)
        
        
    def updateShader(self, cam):
        self.shader.use()
        self.shader.updateCam(cam)
        #for b in self.bodies:
            #self.shader.updatePos(b.posWorld.get())
        
    def updateBodies(self, deltaT):
        counter = 0
        for b in self.bodies:
            b.update(deltaT, counter)
            counter += 1
            
    def draw(self):

        self.shader.use()
        self.texture.bind()
        self.mesh.draw()
        









