#version 330
in vec3 inposition;
in vec2 inTexCord;
in vec3 incolor;

out vec4 color;
out vec2 outTexCord;
        
void main(){
    gl_Position = vec4(inposition, 1.0f);
    outTexCord = inTexCord;
    color = vec4(incolor,1.0f);
}
