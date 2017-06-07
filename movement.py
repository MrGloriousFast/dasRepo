import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import obj, shader, movement
from display import *
import pyrr

class WorldModel():
    def __init__(self, pos= [0,0,0], rot= [0,0,0], scale = [1.0,1.0,1.0]):
        
        #these define the position, rotation and scale
        self.pos = numpy.array(pos,dtype='float32')
        self.rot = numpy.array(rot,dtype='float32')
        self.scale = numpy.array(scale,dtype='float32')
                
    def get(self):
       #generate the world matrix
       #position
        pos   = pyrr.matrix44.create_from_translation(self.pos)
        
       #rotation
        rotx  = pyrr.matrix44.create_from_x_rotation( self.rot[0])
        roty  = pyrr.matrix44.create_from_y_rotation( self.rot[1])
        rotz  = pyrr.matrix44.create_from_z_rotation( self.rot[2])
        #matRot = rotz * roty * rotz
        matRot = numpy.dot(rotz, roty)
        matRot = numpy.dot(matRot, rotx)
        
       #scale
        scale = pyrr.matrix44.create_from_scale(self.scale)       
        
       #matWorld = pos * matRot * scale
        matWorld = numpy.dot(pos, matRot)
        matWorld = numpy.dot(matWorld, scale)
        return matWorld
        
#    def rotate(self, rot):
#    def move(self): 
#    def scale(self):
