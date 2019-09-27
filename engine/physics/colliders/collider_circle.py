from engine.math.utils import * 
from engine.physics.colliders.collider import *
from engine.physics.colliders.collision_resolver import * 

class ColliderCircle(Collider):
    def __init__(self, x, y, r):
        super().__init__(Vect2D(x, y))
        self._r = r

    def check_collision(self, obj):
        if isinstance(obj, ColliderCircle):
            return circle_circle(self, obj)
        else:
            raise Exception("Invalid object passed / Unsupported collision shape.")