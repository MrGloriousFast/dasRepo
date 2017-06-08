#version 330
in vec3 inposition;
in vec2 intexcord;

uniform mat4 worldmodel;
uniform mat4 camera;

out vec2 texCord0;

void main(){
    gl_Position = camera * worldmodel * vec4(inposition, 1.0f);
//    gl_Position = worldmodel * vec4(inposition, 1.0f);
//  gl_Position = vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
