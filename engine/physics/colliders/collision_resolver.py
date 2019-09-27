from engine.math.utils import *

################################################################
#### Collision object ##########################################
################################################################
class Collision():
    def __init__(self):
        self.contact_point = None   # Contact point
        self.normal = None          # Normal vector of the contact point
        self.depth = None           # Depth of object penetration
        self.collider = None        # Collider we hit
        self.game_object = None     # Game object whose collider you are colliding with

################################################################
#### Collision resolvers #######################################
################################################################
def circle_circle(cir1, cir2):
    if cir1._pos.point_distance(cir2._pos) < (cir1._r + cir2._r):
        # Handle collision
        collision = Collision()
        
        collision.normal = (cir2._pos - cir1._pos).normalize()
        collision.contact_point = cir1._pos + collision.normal * cir1._r
        collision.collider = cir2
        collision.depth = (cir1._r + cir2._r) - cir1._pos.point_distance(cir2._pos)

        return collision

def circle_rectangle(cir, rec):
    pass

def circle_convex(cir, rec):
    pass

def rectangle_rectangle(rec1, rec2):
    pass

def rectangle_convex(rec, cir):
    pass

def convex_convex(cir1, cir2):
    pass