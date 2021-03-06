import pygame,math, numpy, random, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
from obj import *
from display import *
from camera import *
from instance import *


def main():

    """
    controls:
    wasd move (relative to view direction)
    mouse look around
    shift fly down
    space fly up
    
    1,2,3 will change render from surfaces to lines/dots
    r stop rotation of cubes
    ESC to quit
    
    """

    #x, y, fps
    dis = Display(1600, 900, "evil engine #9", 60)#10+50*random.random()

    cam = Camera((dis.w, dis.h))

    #create a group for cubes
    shader = AShader(os.path.join('shaders','default'))
    tex = Texture(os.path.join('res','sky.png'))
    c = Cube() # we use this as a blue print for all other cubes
    cubes = Instances(c.verticies, c.texcords, c.verticies, shader, tex)

    #create more cubes
    number_cubes = 50000
    for i in range(0, number_cubes):
        pos   = [(random.random()-0.5)*1000.,(random.random()-0.5)*1000.,(random.random()-0.5)*1000.]
        rot   = [(random.random()-0.5)*500.,(random.random()-0.5)*500.,(random.random()-0.5)*500.]
        s     = 0.1+(random.random()**10)*10.0
        scale = [s,s,s]    
        p = WorldModel(pos,rot,scale)
        cubes.append(p)
        if( i%int(number_cubes/10) ==0 ):
            print("loading...", int(100*i/number_cubes), "%" , i)
    cubes.createBuffer_pos()
    
    #capture mouse
    pygame.mouse.set_pos(dis.w/2., dis.w/2)
    pygame.event.get(pygame.MOUSEMOTION) # flush the last movement from the mouse events
    pygame.mouse.set_visible(False)
    
    #create a plane
    #plane = Plane((-500,0,-500), (1000,0,0), (0,0,1000), 100, 100)
        
    while True:
        #start measuring how long this loop will take and clear the screen
        dis.clear()

        #all keyboard and mouse stuff goes there
        userInput(cam, dis)
        
        cubes.updateShader(cam)
        #cubes.updateBodies(dis.deltaT)# very expensive for cpu!!    
        cubes.render()
        
        #plane.update(dis.deltaT, cam)
        #plane.render()


        #for profiling we will end after init time
        #pygame.quit()
        #quit()

        #finisht the frame
        dis.flip()

def userInput(camera, display):
    deltaT = display.deltaT
    #keyboard down presses
    pressed = pygame.key.get_pressed()    
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
        if event.type == pygame.MOUSEMOTION:
        
            x, y = event.rel
            event.pos = (display.w/2,display.h/2)

            #look around
            if( abs(x)>1 ):
                camera.turnRight( -x*deltaT)
            if( abs(y)>1 ):
                camera.turnUp(    -y*deltaT)

            #capture mouse
            pygame.mouse.set_pos(display.w/2., display.w/2)
            pygame.event.get(pygame.MOUSEMOTION) #steal the new mouse event and do nothing with it to reset it
            #print()
            #print(camera.posWorld.getString())
            #print(camera.view())

    #back forth
    if pressed[pygame.K_w]:
        camera.forward(deltaT)
    if pressed[pygame.K_s]:
        camera.forward(-deltaT)

    #up, down
    if pressed[pygame.K_SPACE]:
        camera.upward(-deltaT)
    if pressed[pygame.K_LSHIFT]:
        camera.upward(deltaT)

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
