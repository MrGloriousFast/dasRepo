import pygame, math, numpy
import random, pyrr
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

class Texture:
    def __init__(self, path):
        #load an image
        img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)

        width, height = img.size
        imgData = numpy.array(img.convert("RGBA"), numpy.uint8)
        
        
        #load texture into buffer
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        #texture wrapping params
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        
        glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, (0.0, 0.0, 0.0, 0.0));  

        #texture filtering params, for scaling up or down
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)   
        
        
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgData)

    #will be used to bind the texture to opengl so that it uses it. Opengl can bind many textures at once.
    def bind(self, unit=0):
        glActiveTexture(GL_TEXTURE0+unit)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
    def destructor(self):
        glDeleteTextures(1)
