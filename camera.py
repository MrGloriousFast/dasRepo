from movement import *
import pyrr, numpy

class Camera():
    def __init__(self, aspect = [16,9], fov = 70, posWorld = WorldModel(), zNear = 0.001, zFar = 1000):

        self.posWorld = posWorld
        #move back a little
        self.posWorld.pos = [0,-1,-10.]         
        #turn camaera to view 0,0,0,
        self.posWorld.rot = [0.,0.,0.]


        self.fov = fov
        self.aspect = aspect 
        self.zNear = zNear
        self.zFar = zFar
        self.perspective =  pyrr.matrix44.create_perspective_projection_matrix(fov, aspect[0]/aspect[1], zNear, zFar, dtype='float32')


        self.speedTurn = 1.
        self.speedMove = 10.   
        
    def position(self):
        return self.posWorld.get()
        
    def view(self):
       #generate the world matrix
       #position
        pos   = pyrr.matrix44.create_from_translation(self.posWorld.pos)
       #rotation
        rotx  = pyrr.matrix44.create_from_x_rotation( self.posWorld.rot[0])
        roty  = pyrr.matrix44.create_from_y_rotation( self.posWorld.rot[1])
        rotz  = pyrr.matrix44.create_from_z_rotation( self.posWorld.rot[2])
        matRot = rotz.dot(roty).dot(rotx)
       #scale
        scale = pyrr.matrix44.create_from_scale(self.posWorld.scale)       
        view = pos.dot(matRot).dot(scale) #is turned around compared to obj
        return view
    
    def projection(self):
        return self.perspective     
        
    def forward(self, distance):
        self.posWorld.moveRel(0,0, distance * self.speedMove)
        
    def upward(self, distance):
        self.posWorld.move(0,distance * self.speedMove, 0)
        
    def sideward(self,distance):
        self.posWorld.moveRel(distance * self.speedMove, 0, 0)

    def turnRight(self,degree):
        self.posWorld.rotateRel(0, degree * self.speedTurn, 0)
        #self.limitAngle()
        
    def turnUp(self,degree):

        self.posWorld.rotateRel(degree,0,0)
        self.limitAngle()
        
    #no back/ behind spins
    def limitAngle(self):
        if(self.posWorld.rot[0]  > numpy.pi/2.):
            self.posWorld.rot[0] = numpy.pi/2.
        if(self.posWorld.rot[0]  < -numpy.pi/2.):
            self.posWorld.rot[0] = -numpy.pi/2.
        if(self.posWorld.rot[2]  > numpy.pi/2.):
            self.posWorld.rot[2] = numpy.pi/2.
        if(self.posWorld.rot[2]  < -numpy.pi/2.):
            self.posWorld.rot[2] = -numpy.pi/2.
        
