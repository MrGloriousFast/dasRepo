import pygame,math
import random, time
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
    FPS = 60
    deltaT = int(1000/FPS)#just a good guess for the first loop
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #Create the camera
    cam = camera.Camera(45, (display[0]/display[1]), 0.1, 50.0)

    #create some cubes
    objs = []
    for x in range(0,10,2):
        for y in range(0,10,2):
            for z in range(0,10,2):
                objs.append(obj.Cube(1.0,(x,y,z)))

    #create particle objects
    p1 = Particle([0,0,0], [0,0,0], [0,0,0])
    pe = ParticleEmitter([1.0,1.0,1.0], Particle, 20, lambda: [random.randint(0,1), random.randint(0,1), random.randint(0,1)], lambda: [random.randint(0,1), random.randint(0,1), random.randint(0,1)])
    glTranslatef(0.0,0.0, -10)

    while True:
        #start measuring how long this loop took
        start = time.time()

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
        for o in objs:
            o.render()
        pe.update()
        p1.update()
        p1.render()
        pygame.display.flip()
        
        #FPS and deltaT calculation
        end = time.time()
        deltaT = end - start
        waittime = int(1000/FPS - deltaT)
        pygame.time.wait(waittime)

main()
