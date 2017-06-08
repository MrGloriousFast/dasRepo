import numpy
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

class Mesh():
    def __init__(self, verticies = []):

        #read the position data and the texture data    
        pos = [] # just positions
        txc = [] #just text coordinates
        for v in verticies:
            pos.extend(v.pos)
            txc.extend(v.texCord)
        
        #arrays that we will give the graka
        self.verticies = numpy.array(pos,dtype='float32')
        self.texCords = numpy.array(txc,dtype='float32')

        #vertix buffer object for position
        glBindBuffer(GL_ARRAY_BUFFER, glGenBuffers(1))
        glBufferData(GL_ARRAY_BUFFER, self.verticies.shape[0]*4, self.verticies, GL_STATIC_DRAW)
    
        glEnableVertexAttribArray(0)
        #..., jump over stuff, start)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    
        #vertix buffer object for texture
        glBindBuffer(GL_ARRAY_BUFFER, glGenBuffers(1))
        glBufferData(GL_ARRAY_BUFFER, self.texCords.shape[0]*4, self.texCords, GL_STATIC_DRAW)
    
        glEnableVertexAttribArray(1)
        #..., jump over stuff, start)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        
    def draw(self):
        #glDrawElements(GL_TRIANGLES, self.indicies.shape[0]*4, GL_UNSIGNED_INT, None)
        glDrawArrays(GL_TRIANGLES, 0, 3)

class Vertex():
    def __init__(self, pos, tcord):
        self.pos = pos
        self.texCord = tcord
