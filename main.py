import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import obj, camera
from ParticleEmitter import *
from Particle import *

def main():
    pygame.display.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    display = (SCREEN_WIDTH,SCREEN_HEIGHT)
    FPS = 60
    deltaT = int(1000/FPS)#just a good guess for the first loop
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #triangle in vertices
    triangle = obj.Triangle()
    
    while True:
        #start measuring how long this loop will take
        start = time.time()

        #all keyboard and mouse stuff goes there
        userInput()

        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
             
        #draw!!!!
        triangle.render()        
        
        #FPS and deltaT calculation
        pygame.display.flip()
        end = time.time()
        deltaT = end - start
        waittime = int(1000/FPS - deltaT)
        if(waittime > 0):
            pygame.time.wait(waittime)
        else:
            #always wait at least one millisec
            pygame.time.wait(1)

def userInput():
    #keyboard down presses
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #mouse turning
    #mouseRel = (x,y)
    mouseRel = pygame.mouse.get_rel()

    #glRotatef(angle,x,y,z)
    turnspeed = 5
    glRotatef(5,mouseRel[0], mouseRel[1], 0)

    if pressed[pygame.K_w]:
        cam.moveForward()

    if pressed[pygame.K_a]:
        cam.moveLeft()

    if pressed[pygame.K_s]:
        cam.moveBackward()

    if pressed[pygame.K_d]:
        cam.moveRight()

#start the main
main()
