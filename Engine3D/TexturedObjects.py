import numpy as np
from OpenGL.arrays.vbo import VBO
from glApp.PyOGLApp import *
from glApp.LoadMesh import *
from glApp.Light import *



vertex_shader = r'''
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
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
in vec3 normal;
in vec3 fragmentPosition;
in vec3 viewPosition;
out vec4 fragColor;

in vec2 UV;
uniform sampler2D tex;

struct light
{
    vec3 position;
    vec3 color;
};

#define NUM_LIGHTS 3
uniform light lightData[NUM_LIGHTS];

vec4 createLight(vec3 lightPosition, vec3 lightColor, vec3 normal, vec3 fragmentPosition, vec3 viewDirection)
{

    //ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;


    //diffuse
    vec3 norm = normalize(normal);
    vec3 lightDirection = normalize(lightPosition - fragmentPosition);
    float diff = max(dot(normal, lightDirection),0);
    vec3 diffuse = diff * lightColor;


    //specular
    float specularStrength = 0.8;
    vec3 reflectDirection = normalize(-lightDirection - norm);
    float spec = pow(max(dot(viewDirection, reflectDirection), 0), 32);
    vec3 specular = specularStrength * spec * lightColor;

    return vec4(color * (ambient + diffuse + specular), 1);

}


void main()
{

    vec3 viewDirection = normalize( viewPosition - fragmentPosition);
    
    fragColor = createLight(lightData[0].position, lightData[0].color, normal, fragmentPosition, viewDirection);
    for(int index=1; index < NUM_LIGHTS; index++)
        fragColor += createLight(lightData[index].position, lightData[index].color, normal, fragmentPosition, viewDirection);

    fragColor = fragColor * texture(tex, UV);
        
}
'''

class TexturedObjects(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.plane=None
        self.cube = None
        self.light = None
        glEnable(GL_CULL_FACE)
        
    def initialise(self):
        self.programId = createProgram(vertex_shader, fragment_shader)
        self.plane = LoadMesh("/home/ubuntu/Projects/CourseMaterials/Engine3D/models/plane.obj",
                              "/home/ubuntu/Projects/CourseMaterials/Engine3D/images/window.png",
                               self.programId,
                               location=pygame.Vector3(0, -1, -2))
        self.cube = LoadMesh("/home/ubuntu/Projects/CourseMaterials/Engine3D/models/cube.obj",
                              "/home/ubuntu/Projects/CourseMaterials/Engine3D/images/crate.png",
                               self.programId,
                               location=pygame.Vector3(0, -2, -2))
        self.light = Light(self.programId, pygame.Vector3(0, 1, 0), pygame.Vector3(1, 1, 1), 0)
        self.camera = Camera(self.programId, self.screenWidth, self.screenHeight)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def cameraInit(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programId)
        self.camera.update()
        self.light.update()
        self.cube.draw()
        self.plane.draw()

TexturedObjects().mainLoop()