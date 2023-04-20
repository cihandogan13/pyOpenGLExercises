#version 330 core
in vec3 position;
in vec3 vertexColor;
in vec3 vertexNormal;
in vec2 vertexUV;
uniform mat4 projectionMat;
uniform mat4 modelMat;
uniform mat4 viewMat;
out vec3 color;
out vec3 normal;
out vec3 fragmentPosition;
out vec3 viewPosition;
out vec2 UV;
void main()
{
    viewPosition = vec3(inverse(modelMat) *
                            vec4(viewMat[3][0], viewMat[3][1], viewMat[3][2], 1));
    gl_Position = projectionMat * inverse(viewMat) * modelMat * vec4(position, 1.0);
    normal = mat3(transpose(inverse(modelMat))) * vertexNormal;
    fragmentPosition = vec3(modelMat * vec4(position, 1.0));
    color = vertexColor;
    UV = vertexUV;
}
