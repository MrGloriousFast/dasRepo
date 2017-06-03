import pygame,math, numpy
import random, time
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
    triangle = numpy.array(
            [-0.5, -0.5 , 0.0,
            0.5, -0.5 , 0.0,
            0.0, 0.5 , 0.0], 
            dtype='float32')
       
    #vertex shader
    #makes a shape out of vertices
    #is a string so we can give this definition to opengl         
    vertex_shader = """
    #version 330
    in vec4 position;
    
    void main(){
        gl_Position = position;
    }
    """
    
    #fragment shader colors
    #makes color and pixels out of shapes
    fragment_shader = """
    #version 330
    
    void main(){
        //r,g,b,alpha
        gl_FragColor = vec4(1.0f,0.0f,0.0f,1.0f);
    }
    """
    
    #one shader takes one vertex shader and one fragment shader
    shader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader,GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader,GL_FRAGMENT_SHADER)
    )
    
    #vertix buffer object
    VBO = glGenBuffers(1) #each buffer has a number, we choose the 1
    glBindBuffer(GL_ARRAY_BUFFER, VBO) #openGl uses our buffer now
    #what kind of buffer, bytes, vertices, drawType
    #drawTypes: 
    #   GL_STATIC_DRAW , vertex does not change. uploaded once
    #   GL_DYNAMIC_DRAW ,vertex does change rarely (often drawn before change)
    #   GL_STREAM_DRAW , vertex changes with each draw
    glBufferData(GL_ARRAY_BUFFER, 36, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(position)
    
    #use the program!
    glUseProgram(shader)
    
    while True:
        #start measuring how long this loop will take
        start = time.time()

        #all keyboard and mouse stuff goes there
        userInput()

        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
             
        #draw!!!!
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        
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
