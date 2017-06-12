import pygame, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

def getTime():
    return  time.perf_counter()

class Display():
    def __init__(self, width, height, title = "TITLE", fps = 30, clearColor = (0.0, 0.0, 0.05, 0.0)):
        pygame.display.init()
        pygame.display.set_caption(title)

        self.w = width
        self.h = height

        self.fps = fps
        self.deltaT = float(1000./fps)#just a good guess for the first loop

        self.frameCount = 0
        self.frameCountOld = 0
        self.frameCountTimer = 0


        screen = pygame.display.set_mode((self.w,self.h), DOUBLEBUF|OPENGL)
        
        glEnable(GL_DEPTH_TEST) #unfuck 3d surfaces, might make it slower
        glClearColor(*clearColor)# that star just unpacks out tuple
    
    def getActualFps(self):

        if (getTime() > 5+self.frameCountTimer):
            #update timer
            delta = getTime() - self.frameCountTimer
            self.frameCountTimer = getTime()
            #
            print("fps: ", (self.frameCount - self.frameCountOld)/delta)
            self.frameCountOld = self.frameCount
   
    def clear(self):
        self.start = getTime()

        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
    def flip(self):
 
        self.frameCount +=1
        

        
        #FPS and deltaT calculation
        pygame.display.flip()
        self.end = getTime()
        self.deltaT = self.end - self.start
        waittime = int(1000./self.fps - self.deltaT)
        if(waittime > 1):
            
            #time.sleep(waittime/1000.)
            time.sleep(0.001)
        else:
            #always wait at least one millisec
            time.sleep(0.001)
        self.getActualFps()

        
    def polygonMode(self, mode):
        if mode == 'line':
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if mode == 'point':
            glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
        if mode == 'fill':
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)    
            
