import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Mesh():
    """
    We dont use indicies with the elemnt buffer yet. Research has shown that it is only useful if you can wrap your texture perfectly around the mesh, or something like that.
    """

    def __init__(self, verticies = [], texCords = [], indicies = []):

        #arrays that we will give the graka
        self.verticies = numpy.array(verticies,dtype='float16')
        self.texCords  = numpy.array(texCords,dtype='float16')
        self.indicies  = numpy.array(indicies,dtype='uint8')
        self.vSize = 2 #bytes per elemnt in an array
        self.tSize = 2 #bytes per elemnt in an array
        self.iSize = 1 #bytes per elemnt in an array

        #print(verticies)
        #print(texCords)
        #print(indicies)

        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*self.tSize, self.texCords, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #elemt buffer object
        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, glGenBuffers(1))
        #glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indicies.shape[0]*iSize, self.indicies, GL_STATIC_DRAW)        
        
    def extend(self, verticies = [], texCords = [], indicies = []):
        #delete old buffer
        self.delete()

        #make a new buffer with the added information
        #arrays that we will give the graka
        self.verticies = numpy.array([*self.verticies,*verticies],dtype='float16')
        self.texCords  = numpy.array([*self.texCords,*texCords],dtype='float16')
        self.indicies  = numpy.array([*self.indicies,*indicies],dtype='uint8')
        self.vSize = 2 #bytes per elemnt in an array
        self.tSize = 2 #bytes per elemnt in an array
        self.iSize = 1 #bytes per elemnt in an array        

        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*self.tSize, self.texCords, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        print(self.verticies.shape[0])

    def delete(self):
        glDeleteBuffers(2, [self.bufferVertex, self.bufferTexture])
       

    def draw(self):

        #vertix buffer object for position
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #vertix buffer object for texture
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_SHORT, ctypes.c_void_p(0))
        glDrawArrays(GL_TRIANGLES, 0, self.verticies.shape[0])

