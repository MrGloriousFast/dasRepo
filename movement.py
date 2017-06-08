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

    #in world coord        
    def rotate(self, dx, dy, dz):
        #todo
        print("rotate in world coord not implemented yet.")
    
    #in world coord
    def move(self, dx, dy, dz): 
        self.pos = [self.pos[0]+dx, self.pos[1]+dy, self.pos[2]+dz]
        
    #relative to direction
    def rotateRel(self, dx, dy, dz):
        self.rot = [self.rot[0]+dx, self.rot[1]+dy, self.rot[2]+dz]
        self.limitRot()

    #relative to direction
    def moveRel(self, dx, dy, dz):
        # rotate a vector 4 by a matrix
        #v = Matrix44.from_x_rotation(np.pi) * Vector4([1.,2.,3.,1.])
        
        rotx  = pyrr.matrix33.create_from_x_rotation( self.rot[0])
        roty  = pyrr.matrix33.create_from_y_rotation( self.rot[1])
        rotz  = pyrr.matrix33.create_from_z_rotation( self.rot[2])
        #matRot = rotz * roty * rotz
        matRot = numpy.dot(rotz, roty)
        matRot = numpy.dot(matRot, rotx)        

        self.pos += numpy.dot(matRot , pyrr.Vector3([dx,dy,dz]))
        
    #always scale into all directions with the same scalar
    def scale(self, scalar):
        self.scale = [self.scale[0]*scalar, self.scale[1]*scalar, self.scale[2]*scalar]

    def limitRot(self):
        self.rot = [
            ((self.rot[0]+numpy.pi) % (2.*numpy.pi))-numpy.pi,
            ((self.rot[1]+numpy.pi) % (2.*numpy.pi))-numpy.pi,
            ((self.rot[2]+numpy.pi) % (2.*numpy.pi))-numpy.pi,
        ]

    def getString(self):
        s = ""
        
        s+="pos:"
        s+= str(self.pos) + "\n"
        
        s+="rot:"
        s+= str(self.rot) + "\n"
        
        s+="scale:"
        s+= str(self.scale) + "\n"
        
        return s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
