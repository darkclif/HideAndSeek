from engine.unit.player_controller import *
from engine.context import *
from pyglet.window import key

class PlayerControllerHuman(PlayerController):
    ###################
    ##### Methods #####
    ###################
    def __init__(self, player_unit):
        super().__init__(player_unit)
    
    def update(self, dt):
        # Movement
        x = int(Context.key_handler[key.RIGHT]) - int(Context.key_handler[key.LEFT])
        y = int(Context.key_handler[key.UP]) - int(Context.key_handler[key.DOWN])
        self._unit.set_move_axis(x, y)