import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Mesh():
    """
    We dont use indicies with the elemnt buffer yet. Research has shown that it is only useful if you can wrap your texture perfectly around the mesh, or something like that.
    """

    def __init__(self, verticies = [], texCords = [], pos = [], indicies = []):

        #arrays that we will give the graka
        self.verticies = numpy.array(verticies,dtype='float16')
        self.texCords  = numpy.array(texCords,dtype='float16')
        self.indicies  = numpy.array(indicies,dtype='uint8')
        self.pos       = numpy.array(pos,dtype = 'float16')
        self.vSize = 2 #bytes per elemnt in an array
        self.tSize = 2 #bytes per elemnt in an array
        self.iSize = 1 #bytes per elemnt in an array
        self.pSize = 2

        #print(verticies)
        #print(texCords)
        #print(indicies)

        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)
        self.bufferPos = glGenBuffers(1)

        self.create()

        #elemt buffer object
        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, glGenBuffers(1))
        #glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indicies.shape[0]*iSize, self.indicies, GL_STATIC_DRAW)        
        
    def extend(self, verticies = [], texCords = [], pos=[], indicies = []):
        #delete old buffer
        self.delete()

        #make a new buffer with the added information
        #arrays that we will give the graka
        self.verticies = numpy.array([*self.verticies,*verticies],dtype='float16')
        self.texCords  = numpy.array([*self.texCords,*texCords],dtype='float16')
        self.indicies  = numpy.array([*self.indicies,*indicies],dtype='uint8')
        self.pos       = numpy.array([*self.pos, *pos],dtype = 'float16')   

        self.create()




    def delete(self):
        glDeleteBuffers(3, [self.bufferVertex, self.bufferTexture, self.bufferPos])
       
       
    def create(self):
        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)
        self.bufferPos = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*self.tSize, self.texCords, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #p0
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferPos)
        glBufferData(GL_ARRAY_BUFFER, self.pos.shape[0]*self.pSize, self.pos, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(0))
        #p1
        glEnableVertexAttribArray(3)
        glVertexAttribPointer(3, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(self.pSize))
        #p2
        glEnableVertexAttribArray(4)
        glVertexAttribPointer(4, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(2*self.pSize))
        #p3
        glEnableVertexAttribArray(5)
        glVertexAttribPointer(5, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(3*self.pSize))                        


    def draw(self):

        #vertix buffer object for position
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #vertix buffer object for texture
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        
        #vertix buffer object for worldModel position
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferPos)
        glVertexAttribPointer(2, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(0))
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferPos)
        glVertexAttribPointer(3, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(self.pSize))

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferPos)
        glVertexAttribPointer(4, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(2*self.pSize))
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferPos)
        glVertexAttribPointer(5, 4, GL_HALF_FLOAT, GL_FALSE, 16*self.pSize, ctypes.c_void_p(3*self.pSize))                        

        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0], GL_UNSIGNED_SHORT, ctypes.c_void_p(0))
        glDrawArrays(GL_TRIANGLES, 0, self.verticies.shape[0])

