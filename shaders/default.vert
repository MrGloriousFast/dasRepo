#version 130
in vec3 inposition; //vertex position in modelspace
in vec2 intexcord;


in vec4 p0;
in vec4 p1;
in vec4 p2;
in vec4 p3;

uniform mat4 worldmodel; //vertexposition in world space





uniform mat4 camera;

out vec2 texCord0;

void main(){
    //gl_Position = projection * view * worldmodel * vec4(inposition, 1.0f);

//    
    
    vec4 pp0 = vec4(1.0f, 0.0f, 0.0f, 0.0f);
    vec4 pp1 = vec4(0.0f, 1.0f, 0.0f, 0.0f);
    vec4 pp2 = vec4(0.0f, 0.0f, 1.0f, 0.0f);
    vec4 pp3 = vec4(0.0f, 0.0f, 0.0f, 1.0f);
    
    mat4 p = mat4(pp0, pp1, pp2, pp3);
    
    gl_Position = camera * p * vec4(inposition, 1.0f);
//    gl_Position = camera * worldmodel * vec4(inposition, 1.0f);
//    gl_Position = worldmodel * vec4(inposition, 1.0f);
//    gl_Position = vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
