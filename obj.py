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
        self.shader = AShader("shaders/default")
        
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
        self.shader = AShader("shaders/default")
        
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

        #all unique vertices
        vList = []
        vList.append([-0.5, -0.5 , -0.5]) #0
        vList.append([ 0.5, -0.5 , -0.5]) #1
        vList.append([ 0.5,  0.5 , -0.5]) #2
        vList.append([-0.5,  0.5 , -0.5]) #3
        vList.append([-0.5, -0.5 ,  0.5]) #4
        vList.append([ 0.5, -0.5 ,  0.5]) #5
        vList.append([ 0.5,  0.5 ,  0.5]) #6
        vList.append([-0.5,  0.5 ,  0.5]) #7


        #indicies we use to render the cube
        index =  [0, 1, 2,#bottom
                  2, 3, 0, 
                  0, 1, 5,#front
                  5, 4, 0,
                  1, 2, 6,#right
                  6, 5, 1,
                  2, 3, 7,#back
                  7, 6, 2,
                  3, 0, 4,#left
                  4, 7, 3,
                  4, 5, 6,#top
                  6, 7, 4]

        v=[] #vertex array
        for i in index:
            v.extend(vList[i])

        
        #construct the cube, an array of 36 vertices
        #one side of the cube is 1/6 of the image
        #image is 192x32 = (6x1)*32 pixel
        s = 1./6.
        #we have to give each triangle three texture coords        
        t = [#1
            0,0,  s,0, s,1,
            s,1,  0,1, 0,0,
            
            #2
            s,0,2*s,0,2*s,1,
            2*s,1,  s,1, s,0,
            
            #3
            2*s,0,  3*s,0, 3*s,1,
            3*s,1,  2*s,1, 2*s,0,
            
            #4
            3*s,0,  4*s,0, 4*s,1,
            4*s,1,  3*s,1, 3*s,0,
            
            #5
            4*s,0,  5*s,0, 5*s,1,
            5*s,1,  4*s,1, 4*s,0,
            
            #6
            5*s,0,  6*s,0, 6*s,1,
            6*s,1,  5*s,1, 5*s,0,]

        index = []
        for i in range(0,36):
            index.append(i)

        #make the mesh
        self.mesh = Mesh(v, t, index)
        
        #load our shader and use it
        self.shader = AShader("shaders/default")
        
        #use a texture
        self.tex = Texture("res/cube.png")
        
        #world position
        self.posWorld = WorldModel([0.,0.,0.], [0,0,0])
        self.posWorld.rotateRel(0,0.7,0)
                    
    def update(self, deltaT, frameCount, cam):
        
        #whirl it around
        if not pygame.key.get_pressed()[K_r]:
            self.posWorld.rotateRel(-0.02, 0.01 , 0.015)
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.get())
                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.tex.bind()
        self.mesh.draw()
            

