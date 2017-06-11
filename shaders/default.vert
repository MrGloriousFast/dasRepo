#version 130
in vec3 inposition; //vertex position in modelspace
in vec2 intexcord;


in vec4 p0;
in vec4 p1;
in vec4 p2;
in vec4 p3;

uniform mat4 worldmodel; //vertexposistion in world space





uniform mat4 camera;

out vec2 texCord0;

void main(){
//gl_Position = projection * view * worldmodel * vec4(inposition, 1.0f);

    mat4 p = mat4(p0, p1, p2, p3);
    
    gl_Position = camera * p * vec4(inposition, 1.0f);
//    gl_Position = camera * worldmodel * vec4(inposition, 1.0f);
//    gl_Position = worldmodel * vec4(inposition, 1.0f);
//    gl_Position = vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
