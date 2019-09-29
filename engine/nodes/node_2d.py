from engine.nodes.node import *
from engine.math.utils import *

class Node2D(Node):
    def __init__(self, pos = Vect2D(0, 0)):
        self._pos = pos
        self._global_pos = Vect2D(0, 0)
    
    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, pos):
        self._pos = pos

