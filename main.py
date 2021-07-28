import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
import time


from Three import *
 
def main():
    three = Three()
    three.Initialze()
    three.Run()
    three.Terminate()
    
if __name__ == "__main__":
    main()
