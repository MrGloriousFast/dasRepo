import pygame, math, numpy
import random, pyrr, time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from texture import *
from shader import AShader
from mesh import *
from movement import *

class Triangle:
    def __init__(self):
        #the triangle as an array of vertices
        #pos(x,y,z)
        #texCord(x,y)
        v = []
        v.append(Vertex(( -0.5, -0.5 ,  0.0), (0.0 , 0.0)))
        v.append(Vertex((  0.5, -0.5 ,  0.0), (10.0 , 0.0)))
        v.append(Vertex((  0.0,  0.5 ,  0.0), (5.0 , 10.0)))
        
        #make the mesh
        self.mesh = Mesh(v)
        
        #load our shader and use it
        self.shader = AShader("shaders/triangle")
        
        #use a texture
        self.tex = Texture("res/awesomeface.png")
        
        #world position
        self.worldPos = WorldModel([0.,0.,0.], [0,0,0])
                    
    def update(self, deltaT, frameCount):
        #update world pos
        self.worldPos.pos[0] = math.sin(time.time())
        self.worldPos.pos[1] = math.cos(time.time())
        #self.worldPos.pos[2] = math.sin(time.time()/5.)
        
        self.worldPos.rot[0] = math.sin(time.time())
        self.worldPos.rot[1] = math.sin(time.time()/3.)
        self.worldPos.rot[2] = math.sin(time.time()/7.)

        self.worldPos.scale = [math.sin(time.time()/3.), 
                               math.sin(time.time()/3.), 
                               math.sin(time.time()/3.)]

        
        #tell the graka about the changes
        self.shader.update(self.worldPos.get())
                    
    def render(self):
        #draw!!!!
        self.shader.use()
        self.tex.bind()
        self.mesh.draw()
            
class Quad:
    def __init__(self):
    
        #create a new texture
        tex = Texture("res/awesomeface.png")
        tex.bind(0)
        
        m = Mesh([-1.0, -1.0 ,  0.0,     1.0 , 0.0 , 0.0,    0.0, 1.0,
              1.0, -1.0 ,  0.0,     0.0 , 1.0 , 0.0,    1.0, 1.0,
              1.0,  1.0 ,  0.0,     0.0 , 0.0 , 1.0,    1.0, 0.0,
             -1.0,  1.0 ,  0.0,     0.0 , 0.0 , 1.0,    0.0, 0.0])
        
        #the quad as a numpy array of vertices
        #X, Y, Z, R, G, B
        self.vertices = numpy.array(
            [-1.0, -1.0 ,  0.0,     1.0 , 0.0 , 0.0,    0.0, 1.0,
              1.0, -1.0 ,  0.0,     0.0 , 1.0 , 0.0,    1.0, 1.0,
              1.0,  1.0 ,  0.0,     0.0 , 0.0 , 1.0,    1.0, 0.0,
             -1.0,  1.0 ,  0.0,     0.0 , 0.0 , 1.0,    0.0, 0.0],
            dtype='float32')
            
        #we indicate which vertex we mean
        indices = numpy.array(
                  [0, 1, 2,
                   2, 3, 0], dtype='uint32')
            
        #vertex shader
        #makes a shape out of vertices
        #is a string so we can give this definition to opengl
        #this is openGL language!  C-style language called GLSL (OpenGL Shading Language).     
        
        sha = AShader('shaders/quad')
                
        #vertix buffer object
        VBO = glGenBuffers(1)
        #type of buffer and then what we want to put isnide
        glBindBuffer(GL_ARRAY_BUFFER, VBO) #openGl uses our buffer now
        #what kind of buffer, bytes, vertices, drawType
        #drawTypes: 
        #   GL_STATIC_DRAW , vertex does not change. uploaded once
        #   GL_DYNAMIC_DRAW ,vertex does change rarely (often drawn before change)
        #   GL_STREAM_DRAW , vertex changes with each draw
        glBufferData(GL_ARRAY_BUFFER, 32*4, self.vertices, GL_STATIC_DRAW)


        #element buffer object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6*4, indices, GL_STATIC_DRAW)

        #positions attribut
        posAttrib = glGetAttribLocation(sha.shader, "inposition")
        glEnableVertexAttribArray(posAttrib)
        glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 8*4,ctypes.c_void_p(0)) 
        # (.. , abstand, offset {normale int aber als ctype})
        
        #farben attribut
        colAttrib = glGetAttribLocation(sha.shader, "incolor")
        glEnableVertexAttribArray(colAttrib)
        glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 8*4, ctypes.c_void_p(4*3))
        
        #texture attrib
        texAttrib = glGetAttribLocation(sha.shader, "inTexCord")
        glEnableVertexAttribArray(texAttrib)
        glVertexAttribPointer(texAttrib, 2, GL_FLOAT, GL_FALSE, 8*4, ctypes.c_void_p(8*3))        

        #use the program!
        #only one program can be active at one time
        #glUseProgram(shader)
        sha.use()
            
    def render(self):
        #draw!!!!
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
            
          


class Cube:
    def __init__(self):
    
    
        #load an image
        img = Image.open("res/cube.png")
        imgData = numpy.array(img.convert("RGBA"), numpy.uint8)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 192, 32, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgData)

        #relative positions in the texture
        s = (1.0/6.0)
        top    = [(0,0), (s,0), (s,s), (0,s)]
        side0  = [(s,0), (2*s,0), (2*s,s), (s,s)]
        side1  = [(2*s,0), (3*s,0), (3*s,s), (2*s,s)]
        side2  = [(3*s,0), (4*s,0), (4*s,s), (3*s,s)]
        side3  = [(4*s,0), (5*s,0), (5*s,s), (4*s,s)]
        bottom = [(5*s,0), (6*s,0), (6*s,s), (5*s,s)]
    
        print(top)
    
    
        #the quad as a numpy array of vertices
        #X, Y, Z, R, G, B
        self.vertices = numpy.array(
             [-0.5, -0.5 ,  -0.5,   random.random() , random.random() , random.random(),
               0.5, -0.5 ,  -0.5,   random.random() , random.random() , random.random(),
               0.5,  0.5 ,  -0.5,   random.random() , random.random() , random.random(),
              -0.5,  0.5 ,  -0.5,   random.random() , random.random() , random.random(),
              
              -0.5, -0.5 ,  0.5,    random.random() , random.random() , random.random(),
               0.5, -0.5 ,  0.5,    random.random() , random.random() , random.random(),
               0.5,  0.5 ,  0.5,    random.random() , random.random() , random.random(),
              -0.5,  0.5 ,  0.5,    random.random() , random.random() , random.random()]
             ,dtype='float32')
            
        #we indicate which vertex we mean to make a triangle
        indices = numpy.array(
                 [0, 1, 2,#bottom
                  2, 3, 0, 
                  0, 1, 5,#front
                  5, 4, 0, 
                  1, 2, 6,#right
                  6, 5, 1,
                  2, 3, 7,#back
                  7, 6, 2,
                  3, 0, 4,#left
                  4, 7, 3,
                  4, 5, 7,#top
                  7, 6, 5]
                  , dtype='uint32')
        
            
        #vertex shader
        #makes a shape out of vertices
        #is a string so we can give this definition to opengl
        #this is openGL language!  C-style language called GLSL (OpenGL Shading Language).     
        vertex_shader = """
        #version 330
        in vec3 position;
        in vec3 color;
        
        uniform mat4 transform;
        
        out vec3 cornerColor;
        
        void main(){
            cornerColor = color;
            gl_Position = transform*vec4(position, 1.0f);
        }
        """
        
        #fragment shader colors
        #makes color and pixels out of shapes
        fragment_shader = """
        #version 330
        in vec3 cornerColor;
        
        out vec4 outColor;
        
        void main(){
            //r,g,b,alpha
            outColor = vec4(cornerColor, 0.0f);
        }
        """
        
        
        #compile shader
        #one shader takes one vertex shader and one fragment shader
        self.shader = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(vertex_shader,GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(fragment_shader,GL_FRAGMENT_SHADER))
        
        #vertix buffer object
        VBO = glGenBuffers(1)
        #type of buffer and then what we want to put isnide
        glBindBuffer(GL_ARRAY_BUFFER, VBO) #openGl uses our buffer now
        #what kind of buffer, bytes, vertices, drawType
        #drawTypes: 
        #   GL_STATIC_DRAW , vertex does not change. uploaded once
        #   GL_DYNAMIC_DRAW ,vertex does change rarely (often drawn before change)
        #   GL_STREAM_DRAW , vertex changes with each draw
        glBufferData(GL_ARRAY_BUFFER, 48*4, self.vertices, GL_STATIC_DRAW)


        #element buffer object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 36*4, indices, GL_STATIC_DRAW)

        #positions attribut
        posAttrib = glGetAttribLocation(self.shader, "position")
        glEnableVertexAttribArray(posAttrib)
        glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 6*4,ctypes.c_void_p(0)) # (.. , abstand, offset {normale int aber als ctype})
        
        #farben attribut
        colAttrib = glGetAttribLocation(self.shader, "color")
        glEnableVertexAttribArray(colAttrib)
        glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(4*3))
        
        #use the program!
        #only one program can be active at one time
        glUseProgram(self.shader)
        
            
    def render(self):
        #draw!!!!
        #12 triangles with 3 vertices each!
        glDrawElements(GL_TRIANGLES, 12*3, GL_UNSIGNED_INT, None)
    
    def update(self, deltaT):

        speedTurn = 0.2

        rotx = pyrr.Matrix44.from_x_rotation(numpy.pi * deltaT* speedTurn)
        roty = pyrr.Matrix44.from_y_rotation(numpy.pi * deltaT* speedTurn)
        
        
        transformLoc = glGetUniformLocation(self.shader, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rotx * roty)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
