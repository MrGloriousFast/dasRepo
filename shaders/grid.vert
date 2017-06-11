#version 130
in vec3 inposition; //vertex position in modelspace

uniform mat4 worldmodel; //vertexposistion in world space
uniform mat4 view; //camaera in worldspace
uniform mat4 projection; //camera view

void main(){
    gl_Position = projection * view * worldmodel * vec4(inposition, 1.0f);
}
