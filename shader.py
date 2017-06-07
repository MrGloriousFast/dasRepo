from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import numpy, pyrr


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
    
        #uniform array
        #uniforms are global variables for the graka
        self.uniforms = []
        self.uniforms.append(glGetUniformLocation(self.program, "worldmodel"))
         
    def update(self, worldmodel):
        #0 -> first uniform we have, aka worldposition
        #1 -> how many uniforms we send in
        #GL_FALSE -> you wanna transpose the matrix?
        glUseProgram(self.program)
        glUniformMatrix4fv(self.uniforms[0], 1, GL_FALSE, worldmodel) 
 
 
         
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
