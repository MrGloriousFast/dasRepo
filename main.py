import pygame,math
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import obj
from ParticleEmitter import *
from Particle import *
import camera

def main():
        pygame.display.init()
        display = (800,600)
        screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        #fov,aspectratio,znear,zfar
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        #Create the camera
        cam = camera.Camera(45, (display[0]/display[1]), 0.1, 50.0)

        #create a cube
        cube = obj.Cube(1.0,(0,0,0))


        #create particle objects
        p1 = Particle([0,0,0], [0,0,0], [0,0,0])
        pe = ParticleEmitter([1.0,1.0,1.0], Particle, 20, lambda: [random.randint(0,1), random.randint(0,1), random.randint(0,1)], lambda: [random.randint(0,1), random.randint(0,1), random.randint(0,1)])
        glTranslatef(0.0,0.0, -10)

        while True:
                #keyboard down presses
                pressed = pygame.key.get_pressed()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 4:
                                        glTranslatef(0,0,0.1)
                                if event.button == 5:
                                        glTranslatef(0,0,-0.1)


                        if pressed[pygame.K_a]:
                            cam.moveLEFT()

                        if pressed[pygame.K_d]:
                            cam.moveRIGHT()

                        if pressed[pygame.K_w]:
                            cam.moveUP()

                        if pressed[pygame.K_s]:
                            cam.moveDOWN()

                #glRotatef(1, 3, 1, 1)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                cube.render()
                pe.update()
                p1.update()
                p1.render()
                pygame.display.flip()
                pygame.time.wait(10)

main()
