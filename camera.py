from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#camera class

class Camera:
	#fov,aspectratio,znear,zfar
	def __init__(self, fov, aspectratio,znear,zfar, position = (0,0,0), direction = (0,0,0)):
		self.fov = fov
		self.pos = position
		self.dir = direction
		gluPerspective(fov, aspectratio, znear, zfar)
		
	def moveUP(self):
		glTranslatef(0,0.1,0)
	
	def moveLEFT(self):
		glTranslatef(-0.1,0,0)
	
	def moveRIGHT(self):
		glTranslatef(0.1,0,0)
	
	def moveDOWN(self):
		glTranslatef(0,-0.1,0)
