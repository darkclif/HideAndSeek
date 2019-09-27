import pyglet.sprite

import engine.resources as res
from engine.physics.colliders import *

class Player():
    ###################
    ##### Vars ########
    ###################
    _speed = 300.0

    ###################
    ##### Methods #####
    ###################
    def __init__(self, color):
        image_map = {
            "red":  res.pawn_1_image,
            "blue": res.pawn_2_image
        }        
        self._sprite = pyglet.sprite.Sprite(img=image_map[color], x=0, y=0)
        
        self._collider = ColliderCircle(0.0, 0.0, 30.0)
        self._collider.on_stay = self.on_collision

        self._axis_x = 0
        self._axis_y = 0

    def draw(self):
        if self._sprite:
            self._sprite.draw()

    def update(self, dt):
        self._update_position(dt)
        self._sprite.position = self._collider._pos.to_array()

    # Movement
    def set_pos(self, x, y):
        self._collider.set_origin(x, y)

    def set_move_axis(self, x, y):
        self._axis_x = x
        self._axis_y = y

    def _update_position(self, dt):
        self._collider._pos += Vect2D(self._speed * dt * self._axis_x, self._speed * dt * self._axis_y)

    # Collision response
    def on_collision(self, collision):
        self._collider._pos += -collision.normal * collision.depth