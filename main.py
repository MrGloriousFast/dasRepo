import pygame,math
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import obj

def main():
	pygame.display.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	#fov,aspectratio,znear,zfar
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	#create a cube
	cube = obj.Cube(1.0,(0,0,0))

	glTranslatef(0.0,0.0, -10)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			#keybuttons move the view
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-0.1,0,0)

				if event.key == pygame.K_RIGHT:
					glTranslatef(0.1,0,0)

				if event.key == pygame.K_UP:
					glTranslatef(0,0.1,0)

				if event.key == pygame.K_DOWN:
					glTranslatef(0,-0.1,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,0.1)
				if event.button == 5:
					glTranslatef(0,0,-0.1)


		#glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		cube.render()
		pygame.display.flip()
		pygame.time.wait(10)

main()
