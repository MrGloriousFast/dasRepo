import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Mesh():
    """
    We dont use indicies with the elemnt buffer yet. Research has shown that it is only useful if you can wrap your texture perfectly around the mesh, or something like that.
    """

    def __init__(self):

        #arrays that we will give the graka
        self.verticies = numpy.array([],dtype='float16')
        self.texCords  = numpy.array([],dtype='float16')

        self.vSize = 2 #bytes per elemnt in an array
        self.tSize = 2 #bytes per elemnt in an array

        #fill the buffers with data
        self.create()

   #fill the buffer
    def create(self):
        #all buffers we use
        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)

        #vertex
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        
        #texture coordinates
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*self.tSize, self.texCords, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(1)
        
        
    def insert(self, verticies = [], texCords = []):
        #delete old buffer
        self.delete()
                
        #make a new buffer with the added information
        #arrays that we will give the graka
        self.verticies = numpy.array([*self.verticies,*verticies],dtype='float16')
        self.texCords  = numpy.array([*self.texCords,*texCords],dtype='float16')
        
        self.create()
       

    def render(self):

        #vertix buffer object for position
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #vertix buffer object for texture
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        
        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_SHORT, ctypes.c_void_p(0))
        glDrawArrays(GL_TRIANGLES, 0, self.verticies.shape[0])

    #remove the buffers
    def delete(self):
        glDeleteBuffers(3, [self.bufferVertex, self.bufferTexture])
        
        
        
        
