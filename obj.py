import pygame, math, numpy
import random, pyrr, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from texture import *
from shader import AShader
from mesh import *
from movement import *

class Triangle:
    def __init__(self):
        #the triangle as an array of vertices
        #pos(x,y,z)
        #texCord(x,y)
        v = [ -0.5, -0.5 ,  0.0,
               0.5, -0.5 ,  0.0,
               0.0,  0.5 ,  0.0]
               
        t =[  0.0,  0.0,
             10.0,  0.0,
              5.0, 10.0]
        
        i = [0,1,2]
        #make the mesh
        self.mesh = Mesh(v, t, i)
        
        #load our shader and use it
        self.shader = AShader("shaders/triangle")
        
        #use a texture
        self.tex = Texture("res/awesomeface.png")
        
        #world position
        self.posWorld = WorldModel([0.,0.,0.], [0,0,0])
                    
    def update(self, deltaT, frameCount, cam):
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.get())
                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.tex.bind()
        self.mesh.draw()
            
class Quad:
    def __init__(self):
        #the triangle as an array of vertices
        #pos(x,y,z)
        #texCord(x,y)
        v = [ -0.5, -0.5 ,  0.0,
               0.5, -0.5 ,  0.0,
               0.5,  0.5 ,  0.0,
              -0.5,  0.5 ,  0.0]
               
        t =[  0.0,  0.0,
             10.0,  0.0,
             10.0, 10.0,
              0.0, 10.0]
        
        i = [0,1,2,
             2,3,0]
        #make the mesh
        self.mesh = Mesh(v, t, i)
        
        #load our shader and use it
        self.shader = AShader("shaders/triangle")
        
        #use a texture
        self.tex = Texture("res/awesomeface.png")
        
        #world position
        self.posWorld = WorldModel([0.,0.,0.], [0,0,0])
                    
    def update(self, deltaT, frameCount, cam):
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.get())
                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.tex.bind()
        self.mesh.draw()
            
          


class Cube:
    def __init__(self):
        #the cube an array of vertices
        v = [-0.5, -0.5 ,  -0.5,
              0.5, -0.5 ,  -0.5,
              0.5,  0.5 ,  -0.5,
             -0.5,  0.5 ,  -0.5,
              
             -0.5, -0.5 ,  0.5,
              0.5, -0.5 ,  0.5,
              0.5,  0.5 ,  0.5,
             -0.5,  0.5 ,  0.5]
        
        
        
        
        
        """
        tried to only texture one side, that works but the other sides are all fucked up.
        They should be only the color of the pixel at 0,0 ...
        """
        #one side of the cube is 1/6 of the image
        s = 1./6.
        #we have to give each triangle three texCords        
        t = [#1
            0,0,  s,0, s,1,
            0,0,  0,1, s,1,
            
            #2
            0,0,  0,0, 0,0,
            0,0,  0,0, 0,0,
            
            #3
            0,0,  0,0, 0,0,
            0,0,  0,0, 0,0,
            
            #6
            0,0,  0,0, 0,0,
            0,0,  0,0, 0,0,
            
            #7
            0,0,  0,0, 0,0,
            0,0,  0,0, 0,0,
            
            #8
            0,0,  0,0, 0,0,
            0,0,  0,0, 0,0]

            




        i =      [0, 1, 2,#bottom
                  2, 3, 0, 
                  0, 1, 5,#front
                  5, 4, 0, 
                  1, 2, 6,#right
                  6, 5, 1,
                  2, 3, 7,#back
                  7, 6, 2,
                  3, 0, 4,#left
                  4, 7, 3,
                  4, 5, 7,#top
                  7, 6, 5]

        #make the mesh
        self.mesh = Mesh(v, t, i)
        
        #load our shader and use it
        self.shader = AShader("shaders/triangle")
        
        #use a texture
        self.tex = Texture("res/cube.png")
        
        #world position
        self.posWorld = WorldModel([0.,0.,0.], [0,0,0])
        #self.posWorld.rotateRel(0,0.7,0)
                    
    def update(self, deltaT, frameCount, cam):
        
        #whirl it around
        self.posWorld.rotateRel(-0.02, 0.01 , 0.01)
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.get())
                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.tex.bind()
        self.mesh.draw()
            

