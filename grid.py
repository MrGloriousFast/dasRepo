import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Grid():        
    def __init__(self, verticies = []):

        #arrays that we will give the graka
        self.verticies = numpy.array(verticies,dtype='float16')
        self.vSize = 2 #bytes per elemnt in an array

        #vertix buffer object for position
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glBindBuffer(GL_ARRAY_BUFFER, 0)

       
        
    def draw(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glDrawArrays(GL_LINES, 0, self.verticies.shape[0])

