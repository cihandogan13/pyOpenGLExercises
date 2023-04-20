from OpenGL.GL import *

def compileShader(shaderType, shaderSource):
    shaderId = glCreateShader(shaderType)
    glShaderSource(shaderId, shaderSource)
    glCompileShader(shaderId)
    compileSuccess = glGetShaderiv(shaderId, GL_COMPILE_STATUS)
    if not compileSuccess:
        errorMessage = glGetShaderInfoLog(shaderId)
        glDeleteShader(shaderId)
        errorMessage = "\n" + errorMessage.decode("utf-8")
        raise Exception(errorMessage)
    return shaderId

# def compile_shader(shader_type, shader_source):
#     shader_id = glCreateShader(shader_type)
#     glShaderSource(shader_id, shader_source)
#     glCompileShader(shader_id)
#     compile_success = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
#     if not compile_success:
#         error_message = glGetShaderInfoLog(shader_id)
#         glDeleteShader(shader_id)
#         error_message = "\n" + error_message.decode("utf-8")
#         raise Exception(error_message)
#     return shader_id

def createProgram(vertexShaderCode, fragmentShaderCode):
    vertexShaderId = compileShader(GL_VERTEX_SHADER, vertexShaderCode)
    fragmentShaderId = compileShader(GL_FRAGMENT_SHADER, fragmentShaderCode)
    programId = glCreateProgram()
    glAttachShader(programId, vertexShaderId)
    glAttachShader(programId, fragmentShaderId)
    glLinkProgram(programId)
    linkSuccess = glGetProgramiv(programId, GL_LINK_STATUS)
    if not linkSuccess:
        info = glGetProgramInfoLog(programId)
        raise RuntimeError(info)
    glDeleteShader(vertexShaderId)
    glDeleteShader(fragmentShaderId)
    return programId




# def create_program(vertex_shader_code, fragment_shader_code):
#     vertex_shader_id = compile_shader(GL_VERTEX_SHADER, vertex_shader_code)
#     fragment_shader_id = compile_shader(GL_FRAGMENT_SHADER, fragment_shader_code)
#     program_id = glCreateProgram()
#     glAttachShader(program_id, vertex_shader_id)
#     glAttachShader(program_id, fragment_shader_id)
#     glLinkProgram(program_id)
#     link_success = glGetProgramiv(program_id, GL_LINK_STATUS)
#     if not link_success:
#         info = glGetShaderInfoLog(program_id)
#         raise RuntimeError(info)
#     glDeleteShader(vertex_shader_id)
#     glDeleteShader(fragment_shader_id)
#     return program_id