import pygame, math, numpy
import random, pyrr
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Triangle:
    def __init__(self):
        #the triangle as an array of vertices
        #X, Y, Z, R, G, B
        self.vertices = numpy.array(
            [-0.5, -0.5 , 0.0, 1.0 , 0.0 , 0.0,
            0.5, -0.5 , -0.0, 0.0 , 1.0 , 0.0,
            0.0, 0.5 , 0.0,  0.0 , 0.0 , 1.0],
            dtype='float32')
            
        #vertex shader
        #makes a shape out of vertices
        #is a string so we can give this definition to opengl
        #this is openGL language!  C-style language called GLSL (OpenGL Shading Language).     
        vertex_shader = """
        #version 330
        in vec3 position;
        in vec3 color;
        
        out vec3 cornerColor;
        
        void main(){
            cornerColor = color;
            gl_Position = vec4(position, 1.0f);
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
            outColor = vec4(cornerColor, 1.0f);
        }
        """
        
        
        #compile shader
        #one shader takes one vertex shader and one fragment shader
        shader = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(vertex_shader,GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(fragment_shader,GL_FRAGMENT_SHADER))
        
        #vertix buffer object
        VBO = glGenBuffers(1) #each buffer has a number, we choose the 1
        #type of buffer and then what we want to put isnide
        glBindBuffer(GL_ARRAY_BUFFER, VBO) #openGl uses our buffer now
        #what kind of buffer, bytes, vertices, drawType
        #drawTypes: 
        #   GL_STATIC_DRAW , vertex does not change. uploaded once
        #   GL_DYNAMIC_DRAW ,vertex does change rarely (often drawn before change)
        #   GL_STREAM_DRAW , vertex changes with each draw
        glBufferData(GL_ARRAY_BUFFER, 18*4, self.vertices, GL_STATIC_DRAW)

        #positions attribut
        posAttrib = glGetAttribLocation(shader, "position")
        glEnableVertexAttribArray(posAttrib)
        glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 6*4,ctypes.c_void_p(0)) # (.. , abstand, offset {normale int aber als ctype})
        
        #farben attribut
        colAttrib = glGetAttribLocation(shader, "color")
        glEnableVertexAttribArray(colAttrib)
        glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(4*3))
        
        #use the program!
        #only one program can be active at one time
        glUseProgram(shader)
        
            
    def render(self):
        #draw!!!!
        glDrawArrays(GL_TRIANGLES, 0, 3)
            
            
            
            
            
class Quad:
    def __init__(self):
        #the quad as a numpy array of vertices
        #X, Y, Z, R, G, B
        self.vertices = numpy.array(
            [-0.5, -0.5 ,  0.0,     1.0 , 0.0 , 0.0,
              0.0, -0.5 ,  0.0,     0.0 , 1.0 , 0.0,
              0.0,  0.5 ,  0.0,     0.0 , 0.0 , 1.0,
             -0.5,  0.5 ,  0.0,     0.0 , 0.0 , 1.0],
            dtype='float32')
            
        #we indicate which vertex we mean
        indices = numpy.array(
                  [0, 1, 2,
                   2, 3, 0], dtype='uint32')
            
        #vertex shader
        #makes a shape out of vertices
        #is a string so we can give this definition to opengl
        #this is openGL language!  C-style language called GLSL (OpenGL Shading Language).     
        vertex_shader = """
        #version 330
        in vec3 position;
        in vec3 color;
        
        out vec3 cornerColor;
        
        void main(){
            cornerColor = color;
            gl_Position = vec4(position, 1.0f);
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
            outColor = vec4(cornerColor, 1.0f);
        }
        """
        
        
        #compile shader
        #one shader takes one vertex shader and one fragment shader
        shader = OpenGL.GL.shaders.compileProgram(
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
        glBufferData(GL_ARRAY_BUFFER, 24*4, self.vertices, GL_STATIC_DRAW)


        #element buffer object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6*4, indices, GL_STATIC_DRAW)

        #positions attribut
        posAttrib = glGetAttribLocation(shader, "position")
        glEnableVertexAttribArray(posAttrib)
        glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 6*4,ctypes.c_void_p(0)) # (.. , abstand, offset {normale int aber als ctype})
        
        #farben attribut
        colAttrib = glGetAttribLocation(shader, "color")
        glEnableVertexAttribArray(colAttrib)
        glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(4*3))
        
        #use the program!
        #only one program can be active at one time
        glUseProgram(shader)
        
            
    def render(self):
        #draw!!!!
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
            
          


class Cube:
    def __init__(self):
        #the quad as a numpy array of vertices
        #X, Y, Z, R, G, B
        self.vertices = numpy.array(
             [0.0,  0.0 ,  0.0,     1.0 , 0.0 , 0.0,
              0.5,  0.0 ,  0.0,     0.0 , 1.0 , 0.0,
              0.5,  0.5 ,  0.0,     0.0 , 0.0 , 1.0,
              0.0,  0.5 ,  0.0,     1.0 , 0.0 , 0.0,
              
              0.0,  0.0 ,  0.5,     1.0 , 0.0 , 0.0,
              0.5,  0.0 ,  0.5,     0.0 , 1.0 , 0.0,
              0.5,  0.5 ,  0.5,     0.0 , 0.0 , 1.0,
              0.0,  0.5 ,  0.5,     1.0 , 0.0 , 0.0]
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
            outColor = vec4(cornerColor, 1.0f);
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
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)
    
    def update(self, deltaT):

        rotx = pyrr.Matrix44.from_x_rotation(numpy.pi * deltaT)
        transformLoc = glGetUniformLocation(self.shader, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rotx)
