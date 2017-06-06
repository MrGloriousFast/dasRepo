import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import obj
from display import *

def main():

    #x, y, fps
    dis = Display(800, 600, 60)
    

    #load out obj
    #cube = obj.Cube()
    quad = obj.Quad()
    #triangle = obj.Triangle()
    
    
    #wireframe mode
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    
    while True:
        #start measuring how long this loop will take and clear the screen
        dis.clear()

        #all keyboard and mouse stuff goes there
        userInput()
             
        #turn the cube
        #cube.update(time.time())
        
        #draw!!!!
        #cube.render()    
        quad.render()    
        
        dis.limitFps()   

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
