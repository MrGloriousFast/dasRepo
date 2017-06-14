#version 330
out vec4 outColor;

uniform sampler2D diffuse;

in vec2 texCord0;

void main(){

  outColor = vec4(0.0f,0.2f,0.0f, 1.0f);
//    outColor = texture2D(diffuse, texCord0);
}
