import pygame, math, numpy, os
import random, pyrr, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from texture import *
from shader import AShader
from movement import *
from grid import *

class Triangle:
    def __init__(self):
        #the triangle as an array of vertices
        #pos(x,y,z)
        #texCord(x,y)
        self.verticies = [ -0.5, -0.5 ,  0.0,
               0.5, -0.5 ,  0.0,
               0.0,  0.5 ,  0.0]
               
        self.texcords =[  0.0,  0.0,
              1.0,  0.0,
               .5,  1.0]
        
        self.idicies = [0,1,2]

        #world position
        self.posWorld = WorldModel()
                    
    def update(self, deltaT, frameCount, cam):
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.view(), cam.projection())
            
class Quad:
    def __init__(self):
        #the triangle as an array of vertices
        #pos(x,y,z)
        #texCord(x,y)
        self.verticies = [ -0.5, -0.5 ,  0.0,
               0.5, -0.5 ,  0.0,
               0.5,  0.5 ,  0.0,
               
               0.5,  0.5 ,  0.0,
              -0.5,  0.5 ,  0.0,
              -0.5, -0.5 ,  0.0]
               
        self.texcords =[  0.0,  0.0,
              1.0,  0.0,
              1.0,  1.0,
              
              1.0,  1.0,
              0.0,  1.0,
              0.0,  0.0]
        
        i = [0,1,2,
             2,3,0]

    def update(self, deltaT, frameCount, cam):
        
        #tell the graka about the changes
        self.shader.update(self.posWorld.get(), cam.view(), cam.projection())
                    
            
          
class Plane:
    #we need three vectors to define a plane
    def __init__(self, basis, v1, v2, h, v):

        b = pyrr.Vector3(basis)
        m = pyrr.Vector3(v1)
        n = pyrr.Vector3(v2)
                
        #add horizontal lines
        verticies = []
        for hh in range(0,h+1):
            x = [*((hh*m/h) )]
            y = [*((hh*m/h) +n)]
            verticies.extend(x)
            verticies.extend(y)
        

        #add vertical lines
        for vv in range(0,v+1):
            x = [*((vv*n/v) )]
            y = [*((vv*n/v) +m)]
            verticies.extend(x)
            verticies.extend(y)            
        
        self.posWorld = WorldModel(b)
        self.shader = AShader(os.path.join('shaders','grid'))
        self.grid = Grid(verticies)
        
        
    def update(self, deltaT, cam):
        #tell the graka about the changes
        self.shader.use()
        self.shader.updatePos(self.posWorld.get())
        self.shader.updateCam(cam)

                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.grid.draw()


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
        self.indicies =  [
                  0, 1, 2,#bottom
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

        self.verticies=[] #vertex array
        for i in self.indicies:
            self.verticies.extend(vList[i])

        
        #construct the cube, an array of 36 vertices
        #one side of the cube is 1/6 of the image
        #image is 192x32 = (6x1)*32 pixel
        s = 1./6.
        #we have to give each triangle three texture coords        
        self.texcords = [

            #2
              s,0,  2*s,0,  2*s,1,
            2*s,1,    s,1,    s,0,

            #5
            4*s,1,  5*s,1, 5*s,0,
            5*s,0,  4*s,0, 4*s,1,
                        
            #3
            2*s,0,  2*s,1, 3*s,1,
            3*s,1,  3*s,0, 2*s,0,
            
            #6
            6*s,0,  5*s,0, 5*s,1,
            5*s,1,  6*s,1, 6*s,0,

            #1
            s,1,  s,0, 0,0,
            0,0,  0,1, s,1,

            #4
            4*s,0,  3*s,0, 3*s,1,
            3*s,1,  4*s,1, 4*s,0]

        
        #world position
        self.posWorld = WorldModel()
        #if you have many cubes you should use the Group render
        #self.mesh = Mesh()
        #self.mesh.insert(self.verticies, self.texcords, self.posWorld.get())
                    
    def update(self, deltaT, counter):
        self.posWorld.rotateRel(0.001*counter,0.001*counter,0.001*counter)
        #self.posWorld.setSize(.01*(0.5+0.5*abs(math.sin(time.time()))))












