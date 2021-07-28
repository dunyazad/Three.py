from OpenGL.GL import *
import OpenGL.GL.shaders

import numpy

class Renderer:
    triangle = None

    def __init__(self):
        pass

    def Initialize(self):
         #            positions        colors
        self.triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0,  0.5, 0.0, 0.0, 0.0, 1.0]
    
        self.triangle = numpy.array(self.triangle, dtype = numpy.float32)
    
        vertex_shader = """
        #version 330
        in vec3 position;
        in vec3 color;
        out vec3 newColor;
        void main()
        {
            gl_Position = vec4(position, 1.0f);
            newColor = color;
        }
        """
    
        fragment_shader = """
        #version 330
        in vec3 newColor;
        out vec4 outColor;
        void main()
        {
            outColor = vec4(newColor, 1.0f);
        }
        """
        shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                                OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, 72, self.triangle, GL_STATIC_DRAW)
    
        position = glGetAttribLocation(shader, "position")
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)
    
        color = glGetAttribLocation(shader, "color")
        glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(color)
    
        glUseProgram(shader)

    def Update(self, timeDelta):
        pass

    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT)
 
        glDrawArrays(GL_TRIANGLES, 0, 3)
