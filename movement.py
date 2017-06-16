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
        self.pos = numpy.array(pos,dtype='float32') #pos in the world
        self.rot = numpy.array(rot,dtype='float32') #rot relative to itself
        self.scale = numpy.array(scale,dtype='float32') #relative to itself

        self.update()

    def get(self):
    
        return self.matWorld

    def update(self):    
       #generate the world matrix
       #position
        pos   = pyrr.matrix44.create_from_translation(self.pos)
        
       #rotation
        rotx  = pyrr.matrix44.create_from_x_rotation( self.rot[0])
        roty  = pyrr.matrix44.create_from_y_rotation( self.rot[1])
        rotz  = pyrr.matrix44.create_from_z_rotation( self.rot[2])
        #matRot = rotx * roty * rotz
        matRot = rotx.dot(roty).dot(rotz)
        
        #for some reason the following two alternatives are even slower!
#        matRot = pyrr.matrix44.create_from_axis_rotation(self.rot, 1) 
#        matRot = pyrr.matrix44.create_from_eulers(self.rot) 

        
       #scale
        scale = pyrr.matrix44.create_from_scale(self.scale)       
        
       #matWorld = pos * matRot * scale
        self.matWorld = scale.dot(matRot).dot(pos)

    #in world coord        
    def rotate(self, dx, dy, dz):
        
        rotx  = pyrr.matrix33.create_from_x_rotation( self.rot[0])
        roty  = pyrr.matrix33.create_from_y_rotation( self.rot[1])
        rotz  = pyrr.matrix33.create_from_z_rotation( self.rot[2])
        #matRot = rotz * roty * rotz
        rotChange = rotx.dot(roty).dot(rotz).dot( pyrr.Vector3([dx,dy,dz]) )

        self.rot += rotChange 
        self.limitRot()


    
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
        posChange = rotz.dot(roty).dot(rotx).dot( pyrr.Vector3([dx,dy,dz]) )

        self.pos += posChange

        
    #always scale into all directions with the same scalar
    def resize(self, scalar):
        self.scale = numpy.array([self.scale[0]*scalar, self.scale[1]*scalar, self.scale[2]*scalar],dtype='float32')


    def setSize(self, size):
        self.scale = numpy.array([size, size, size],dtype='float32')


    def limitRot(self):
        self.rot = [
            ((self.rot[0]+numpy.pi) % (2.*numpy.pi))-numpy.pi,
            ((self.rot[1]) % (2.*numpy.pi)), #0 to 2pi
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
