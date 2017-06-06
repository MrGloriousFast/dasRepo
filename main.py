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

    #load out obj
    #cube = obj.Cube()
    quad = obj.Quad()
    #triangle = obj.Triangle()
    
    #make it not buggy
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.05, 0.0); #almost black but not bloack so we can see black things
    
    #wireframe mode
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    
    while True:
        #start measuring how long this loop will take
        start = time.time()

        #all keyboard and mouse stuff goes there
        userInput()

        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
             
        #turn the cube
        #cube.update(time.time())
        
        #draw!!!!
        #cube.render()    
        quad.render()    
        
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
    #mouseRel = pygame.mouse.get_rel()

    if pressed[pygame.K_1]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
    if pressed[pygame.K_2]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if pressed[pygame.K_3]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


#start the main
main()
