import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import time
import numpy
import win32api
import win32.lib.win32con as win32con

from Renderer import *

class Three:
    window = None
    renderer = None

    def __init__(self):
        pass

    def Initialze(self, windowWidth = 800, windowHeight = 600):
        if not glfw.init():
            return

        self.window = glfw.create_window(windowWidth, windowHeight, "Three.py window", None, None)

        # send window to center of current monitor
        pos = win32api.GetCursorPos()
        monitors = win32api.EnumDisplayMonitors(None, None)

        for index, monitor in enumerate(monitors):
            (left, top, right, bottom) = monitor[2]
            if (left <= pos[0] and pos[0] <= right) and (top <= pos[1] and pos[1] <= bottom):
                wx = left + (right - left) / 2 - windowWidth / 2
                wy = top + (bottom - top) / 2 - windowHeight / 2
                glfw.set_window_pos(self.window, int(wx), int(wy))
                break

        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)
        glfw.swap_interval(0)

        self.renderer = Renderer()
        self.renderer.Initialize()

    def Run(self):
        glClearColor(0.2, 0.3, 0.2, 1.0)
 
        now = time.time_ns()
        lastTime = time.time_ns()

        while not glfw.window_should_close(self.window):
            glfw.poll_events()
 
            now = time.time_ns()
            timeDelta = now - lastTime
            lastTime = now

            # print(str(timeDelta / 1000000))

            self.renderer.Update(timeDelta)
            self.renderer.Render()
 
            glfw.swap_buffers(self.window)

    def Terminate(self):
        glfw.terminate()
