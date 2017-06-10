#version 130
in vec3 inposition; //vertex position in modelspace
in vec2 intexcord;

uniform mat4 worldmodel; //vertexposistion in world space
uniform mat4 view; //camaera in worldspace
uniform mat4 projection; //camera view

out vec2 texCord0;

void main(){
gl_Position = projection * view * worldmodel * vec4(inposition, 1.0f);
//    gl_Position = camera * worldmodel * vec4(inposition, 1.0f);
//    gl_Position = worldmodel * vec4(inposition, 1.0f);
//    gl_Position = vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
