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
        self.modelMats = numpy.array([],dtype='float32')

        self.vSize = 2 #bytes per elemnt in an array
        self.tSize = 2 #bytes per elemnt in an array
        self.mSize = 4 #bytes per elemnt in an array

        #fill the buffers with data
        self.create()

   #fill the buffer
    def create(self):
    
        #all buffers we use
        self.bufferVertex = glGenBuffers(1)
        self.bufferTexture = glGenBuffers(1)
        self.bufferModel = glGenBuffers(1)

        #vertex
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*self.vSize, self.verticies, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(0)
        
        #texture coordinates
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*self.tSize, self.texCords, GL_STATIC_DRAW)    
        glEnableVertexAttribArray(1)
        
        #modelMatrix
        #print("self.modelMats.shape[0]", self.modelMats.shape[0])
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferModel)
        glBufferData(GL_ARRAY_BUFFER, self.modelMats.shape[0]*self.mSize, self.modelMats, GL_STATIC_DRAW)
        
        
        
        
        
        
        
        

        glEnableVertexAttribArray(3)
        glEnableVertexAttribArray(4)
        glEnableVertexAttribArray(5) 
        glEnableVertexAttribArray(6) 



            
        
        
        
        
        
        
        
        
        
        
    def insert(self, verticies , texCords , modelMats ):
        #delete old buffer
        self.delete()
                
        temp = []
        for i in modelMats:
            temp.extend(i)
        modelMats = temp
                
        #make a new buffer with the added information
        #arrays that we will give the graka
        self.verticies = numpy.array([*self.verticies,*verticies],dtype='float16')
        self.texCords  = numpy.array([*self.texCords,*texCords],dtype='float16')
        self.modelMats  = numpy.array([*self.modelMats,*modelMats],dtype='float32')
        
        self.create()
       

    def bind(self):

        #vertix buffer object for position
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferVertex)
        glVertexAttribPointer(0, 3, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #vertix buffer object for texture
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferTexture)
        glVertexAttribPointer(1, 2, GL_HALF_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #4 vertix buffer for the 4 vec4 vectors that will form the worldmodelmatrix
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferModel)
        vec4Size = 4*self.mSize
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(0))
        glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(vec4Size))
        glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(2*vec4Size))
        glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(3*vec4Size))

        glVertexAttribDivisor(3, 1)
        glVertexAttribDivisor(4, 1)
        glVertexAttribDivisor(5, 1)
        glVertexAttribDivisor(6, 1)

    def render(self):

        #glDrawArrays(GL_TRIANGLES, 0, self.verticies.shape[0])
        #print("self.verticies.shape[0]", self.verticies.shape[0], "self.modelMats.shape[0]", self.modelMats.shape[0])
#        glDrawElementsInstanced(GL_TRIANGLES, self.verticies.shape[0], GL_UNSIGNED_INT, ctypes.c_void_p(0), self.modelMats.shape[0])
        glDrawArraysInstanced(GL_TRIANGLES, 0, self.verticies.shape[0], self.modelMats.shape[0])

    #remove the buffers
    def delete(self):
        glDeleteBuffers(3, [self.bufferVertex, self.bufferTexture])
        
        
        
        
