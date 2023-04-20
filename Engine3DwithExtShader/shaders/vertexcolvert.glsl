#version 330 core
in vec3 position;
in vec3 vertexColor;
uniform mat4 projectionMat;
uniform mat4 modelMat;
uniform mat4 viewMat;
out vec3 color;

void main()
{
    gl_Position = projectionMat * inverse(viewMat) * modelMat * vec4(position,1);
    color = vertexColor;
}