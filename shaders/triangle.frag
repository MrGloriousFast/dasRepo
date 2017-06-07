#version 330
out vec4 outColor;

uniform sampler2D diffuse;

in vec2 texCord0;

void main(){

//  outColor = vec4(1.0f,0.0f,0.0f, 1.0f);
    //unit ist eine von vielen texturen die man geladen hat, hier unit =0
    outColor = texture2D(diffuse, texCord0);
}
