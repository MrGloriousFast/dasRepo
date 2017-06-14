from OpenGL.GL import *
from OpenGL.GLU import *
from texture import *
from shader import AShader
import numpy as np

def mat_to_array(mat):
    temp = []
    for i in mat:
        for j in i.get():
            temp.extend(j)

    return temp

class Instances:
    def __init__(self, verticies, texcords, normals, shader, texture):
        #everyhting they share
        self.verticies = verticies
        self.texcords  = texcords
        self.normals   = normals
        self.shader    = shader
        self.texture   = texture

        #all world positions, empty in init
        self.inst_pos = []
        self.instances = 0
    
        #create all static buffers
        self.createBuffer()


    #add another instance
    def append(self, worldpos):
        self.inst_pos.append(worldpos)
        self.instances += 1
    
    def updateShader(self, cam):
        self.shader.use()
        self.shader.updateCam(cam)
    
    """
    buffer for static data
    """
    def createBuffer(self):
            
        #create a buffer
        # we will use only one buffer for all static things that are the same for each instance
        self.buffer = glGenBuffers(1)

        #bind it, aka use it
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
        
        #sort the data
        interleaved = []
        for i in range(0,int(len(self.verticies)/3)):
            #all three vertex floats afet each other
            interleaved.append(self.verticies[i*3])
            interleaved.append(self.verticies[i*3+1])
            interleaved.append(self.verticies[i*3+2])
            #all two texture coords after each other
            interleaved.append(self.texcords[i*2])
            interleaved.append(self.texcords[i*2+1])
            #all three normal floats after each other
            interleaved.append(self.normals[i*3]) 
            interleaved.append(self.normals[i*3+1]) 
            interleaved.append(self.normals[i*3+2])        
        
        #make this list so that openGl can read it
        inter = np.array(interleaved, dtype="float32")
        self.size = 4 #bytes  

        #print("inter.shape[0]", inter.shape[0])
        #print("divided by 8:", inter.shape[0]/8)

        #fill the buffer
        glBufferData(GL_ARRAY_BUFFER, self.size*inter.shape[0], inter, GL_STATIC_DRAW)

        #24 floats with 4 byte each
        #vec3 inposition      3
        #vec2 intexcord       2
        #vec3 normal          3
        #mat4 instanceMatrix 16
        self.buffer_step = self.size*8

        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2) 

        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)



    """
    buffer for changing data
    it can be bigger or smaller than the other buffer, depending on the number of instances.
    """
    def createBuffer_pos(self):
        
        #we will use another buffer for all data that changes often (aka world position)
        self.buffer_pos = glGenBuffers(1)

        #bind it, aka use it
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_pos)

        #how much data is in one "step" or stride
        self.buffer_step_pos = self.size*16

        #we have to break up the mat4 into 4 vectors
        interleaved = []
        pos = mat_to_array(self.inst_pos) 
        
        #print()
        #print(self.inst_pos[0].get())
        
               
        for i in range(0,int(len(pos))):
            #column vector
            interleaved.append(pos[i])
        

        #print(interleaved)


        #make this list so that openGl can read it
        inter = np.array(interleaved, dtype="float32")
        self.size = 4 #bytes  

        #print("inter.shape[0] POS", inter.shape[0])
        #print("divided by 16:", inter.shape[0]/16)

        #fill the buffer
        glBufferData(GL_ARRAY_BUFFER, self.size*inter.shape[0], inter, GL_DYNAMIC_DRAW) #might be changed to even more dynamic changes

        glEnableVertexAttribArray(3)
        glEnableVertexAttribArray(4)
        glEnableVertexAttribArray(5) 
        glEnableVertexAttribArray(6) 

        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def delete(self):
        glDeleteBuffers(1, self.buffer)


    def bind(self):
        #make sure we use the correct shader and texture
        self.shader.use()
        self.texture.bind()

        """ STATIC MODEL """    
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        #now we need to specify where to look into the buffer if you want one specific float:
        #vertex data
        offset = 0
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.buffer_step, ctypes.c_void_p(offset))
        #texture data
        offset = 3 * self.size
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.buffer_step, ctypes.c_void_p(offset))
        #normdata
        offset = (3+2) * self.size
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.buffer_step, ctypes.c_void_p(offset))       

        #tell open gl that we change these with each vertex loop (0)
        glVertexAttribDivisor(0,0)
        glVertexAttribDivisor(1,0)
        glVertexAttribDivisor(2,0)

        """ POSITION """
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_pos)
        
        #set the pointer correctly
        #c0
        offset = (0) * self.size
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, self.buffer_step_pos, ctypes.c_void_p(offset))
        #c1
        offset = (4) * self.size
        glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, self.buffer_step_pos, ctypes.c_void_p(offset))
        #c2
        offset = (4+4) * self.size
        glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, self.buffer_step_pos, ctypes.c_void_p(offset))
        #c3
        offset = (4+4+4) * self.size
        glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, self.buffer_step_pos, ctypes.c_void_p(offset))

        #these the ones we want to change only once per instance
        glVertexAttribDivisor(3,1)
        glVertexAttribDivisor(4,1)
        glVertexAttribDivisor(5,1)
        glVertexAttribDivisor(6,1)

        
        

    def render(self):
    
        #use all correct pointer and shader etc
        self.bind()
        
        #draw ett!
        #mode = GL_TRIANGLES
        first = 0
        count = len(self.verticies)
        primcount = self.instances
        glDrawArraysInstanced(GL_TRIANGLES, first, count, primcount)
        
        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
