from EventDispatcher import *

_object3DId = 0

class Object3D(EventDispatcher):
    def __init__(self):
        global _object3DId
        _object3DId = _object3DId + 1
        self.id = _object3DId

