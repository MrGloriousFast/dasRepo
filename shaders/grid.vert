#version 330
in vec3 inposition; //vertex position in modelspace

uniform mat4 worldmodel; //vertexposistion in world space
uniform mat4 camera; //camera view

void main(){
    gl_Position = camera * worldmodel * vec4(inposition, 1.0f);
}
