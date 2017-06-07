import pygame, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Display():
    def __init__(self, width, height, fps = 30, title = "TITLE", clearColor = (0.0, 0.0, 0.05, 0.0)):
        pygame.display.init()
        pygame.display.set_caption(title)
        self.w = width
        self.h = height
        self.fps = fps
        self.deltaT = float(1000/fps)#just a good guess for the first loop
        self.frameCount = 0
        screen = pygame.display.set_mode((self.w,self.h), DOUBLEBUF|OPENGL)
        
        glEnable(GL_DEPTH_TEST)
        glClearColor(*clearColor)# that star just unpacks out tuple
    
    def clear(self):
        self.start = time.time()

        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
    def flip(self):
 
        self.frameCount +=1
        
        #FPS and deltaT calculation
        pygame.display.flip()
        self.end = time.time()
        self.deltaT = self.end - self.start
        waittime = int(1000/self.fps - self.deltaT)
        if(waittime > 0):
            pygame.time.wait(waittime)
        else:
            #always wait at least one millisec
            pygame.time.wait(1)
        
    def polygonMode(self, mode):
        if mode == 'line':
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if mode == 'point':
            glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
        if mode == 'fill':
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)    
            
