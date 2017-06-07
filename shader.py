from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *


class AShader():
    def __init__(self, path):
        
        self.program = glCreateProgram()
        self.s = []
        self.s.append(self.createShader(self.read(path+".vert"), GL_VERTEX_SHADER))
        self.s.append(self.createShader(self.read(path+".frag"), GL_FRAGMENT_SHADER))
    
        for shad in self.s:
            glAttachShader(self.program, shad)
    
        self.shader = OpenGL.GL.shaders.compileProgram(self.s[0], self.s[1])
    
        glBindAttribLocation(self.program, 0, "inposition")
        glBindAttribLocation(self.program, 1, "intexcord")        
    
        glLinkProgram(self.program)
        glValidateProgram(self.program)
    
    #openGl use this shader!
    def use(self):
        glUseProgram(self.program)
    
   #maybe not needed in python
    def destruct(self):
        for shad in self.s:
            glDetachShader(self.program, shad)
            glDeleteShader(shad)
        glDeleteProgram(self.program)
    
    #create a new shader
    def createShader(self, text, shaderType):
        shader = glCreateShader(shaderType)
        if(shader == 0):
            print("shader creation failed!")

        #compile shader
        shader = OpenGL.GL.shaders.compileShader(text,shaderType)


        return shader
    
    #could be useful but i dont know how to make it yet
    def checkError(self):
        print('todo')
        
    #just opens a shader file
    def read(self, path):
        return open(path,'r').readlines()
