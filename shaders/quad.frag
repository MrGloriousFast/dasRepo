#version 330
in vec2 outTexCord;
in vec4 color;
uniform sampler2D samplerTex1;
//uniform sampler2D samplerTex2;

out vec4 outColor;

void main(){
    //r,g,b,alpha
    outColor = texture(samplerTex1, outTexCord)*color;
    //outColor = mix(texture(samplerTex1, outTexCord), texture(samplerTex2, outTexCord), 0.2)
}
