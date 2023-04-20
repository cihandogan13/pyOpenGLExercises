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

    fragColo r = fragColor * texture(tex, UV);
        
}