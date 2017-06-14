#version 330
in vec3 inposition; //vertex position in modelspace
in vec2 intexcord;
in vec3 normal; //we dont use it yet

in vec4 c0;
in vec4 c1;
in vec4 c2;
in vec4 c3;

uniform mat4 camera;

out vec2 texCord0;

void main(){
    //using instancing baby
    mat4 worldpos = mat4(c0, c1, c2, c3)
    gl_Position = camera * worldpos * vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
