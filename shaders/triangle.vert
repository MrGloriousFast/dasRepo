#version 330
attribute vec3 inposition;
attribute vec2 intexcord;

out vec2 texCord0;

void main(){
    gl_Position = vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
