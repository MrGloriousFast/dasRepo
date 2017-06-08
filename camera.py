from movement import *
import pyrr, numpy

class Camera():
    def __init__(self, aspect = [16,9], fov = 70, posWorld = WorldModel(), zNear = 0.05, zFar = 1000):

        self.posWorld = posWorld
        #move back a little
        self.posWorld.pos = [0,0,-2]         
        #turn camaera to view 0,0,0,
        self.posWorld.rot = [0.,0.,0.]


        self.fov = fov
        self.aspect = aspect 
        self.zNear = zNear
        self.zFar = zFar
        self.perspective =  pyrr.matrix44.create_perspective_projection_matrix(fov, aspect[0]/aspect[1], zNear, zFar, dtype=None)


        self.speedTurn = 1.
        self.speedMove = 10.        
        
    #returns the perspective matrix                
    def get(self):
        return numpy.dot(self.posWorld.get(), self.perspective)
        
    def forward(self, distance):
        self.posWorld.moveRel(0,0, distance * self.speedMove)
        
    def upward(self, distance):
        self.posWorld.move(0,-distance * self.speedMove, 0)
        
    def sideward(self,distance):
        self.posWorld.moveRel(distance * self.speedMove, 0, 0)

    def turnRight(self,degree):
        self.posWorld.rotateRel(0, degree * self.speedTurn, 0)
        self.limitAngle()
        
    def turnUp(self,degree):
        self.posWorld.rotateRel(degree * self.speedTurn,0,0)
        self.limitAngle()
        
    #no back/ behind spins
    def limitAngle(self):
        if(self.posWorld.rot[0]  > numpy.pi/2.):
            self.posWorld.rot[0] = numpy.pi/2.
        if(self.posWorld.rot[0]  < -numpy.pi/2.):
            self.posWorld.rot[0] = -numpy.pi/2.
        
