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


    vec4 cc0 = vec4(1.0f, 0.0f, 0.0f, 0.0f);
    vec4 cc1 = vec4(0.0f, 1.0f, 0.0f, 0.0f);
    vec4 cc2 = vec4(0.0f, 0.0f, 1.0f, 0.0f);
    vec4 cc3 = vec4(-38.748535692767597f, 3.0751020962635911f, 34.201980565143067f, 1.0f);
    
    mat4 worldpos = mat4(c0, c1, c2, c3);
    gl_Position = camera * worldpos * vec4(inposition, 1.0f);
    texCord0 = intexcord;
}
