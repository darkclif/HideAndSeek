from engine.math.utils import *

class Collider():
    ###################################################
    ##### Methods #####################################
    ###################################################
    def __init__(self, pos):
        self._pos = pos

        self.on_enter = None
        self.on_stay = None
        self.on_exit = None

    # Check collision with other object
    def check_collision(self, obj):
        raise Exception("Invalid instance of abstract class.")

    # Position
    def get_origin(self):
        return self._pos

    def set_origin(self, x, y):
        self._pos = Vect2D(x, y)