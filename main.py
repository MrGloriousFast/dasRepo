import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import obj, shader, movement
from display import *
from camera import *

def main():

    #x, y, fps
    dis = Display(800, 600, 60, "evil engine #9")

    cam = Camera((800, 600))

    #load out obj
    #cube = obj.Cube()
    #quad = obj.Quad()
    triangle = obj.Triangle()
    
    #capture mouse
    pygame.mouse.set_pos(dis.w/2., dis.w/2)
    pygame.event.get(pygame.MOUSEMOTION)
        
    while True:
        #start measuring how long this loop will take and clear the screen
        dis.clear()

        #all keyboard and mouse stuff goes there
        userInput(cam, dis)
             
        #turn the cube
        #cube.update(time.time())
        
        #draw!!!!
        #cube.render()    
        #quad.render()   
        triangle.update(dis.deltaT, dis.frameCount, cam) 
        triangle.render()
        
        dis.flip()   

def userInput(camera, display):
    deltaT = display.deltaT
    #keyboard down presses
    pressed = pygame.key.get_pressed()    
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION:
        
            x, y = event.rel
            event.pos = (display.w/2,display.h/2)

            #look around
            camera.turnRight( -x*deltaT)
            camera.turnUp(    -y*deltaT)

            #capture mouse
            pygame.mouse.set_pos(display.w/2., display.w/2)
            pygame.event.get(pygame.MOUSEMOTION)
            
            print(camera.posWorld.getString())

    #back forth
    if pressed[pygame.K_w]:
        camera.forward(deltaT)
    if pressed[pygame.K_s]:
        camera.forward(-deltaT)

    #up, down
    if pressed[pygame.K_SPACE]:
        camera.upward(deltaT)
    if pressed[pygame.K_LSHIFT]:
        camera.upward(-deltaT)

    #left right
    if pressed[pygame.K_a]:
        camera.sideward(deltaT)
    if pressed[pygame.K_d]:
        camera.sideward(-deltaT)

    #change openGL polygon mode
    if pressed[pygame.K_1]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
    if pressed[pygame.K_2]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if pressed[pygame.K_3]:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


#start the main
main()
