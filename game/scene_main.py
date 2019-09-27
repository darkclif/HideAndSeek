import random
#from pyglet import clock

from engine.scene.scene import *

from engine.unit.player import *
from engine.unit.player_controller_ai import *
from engine.unit.player_controller_human import *

class SceneMain(Scene):
    ###################################################
    ##### Methods #####################################
    ###################################################
    def __init__(self, scenes_stack):
        super().__init__(scenes_stack)
        self._setup()
        
    #### Scene setup ##################################
    def _setup(self):
        self._players = []
        self._players_controllers = []

        self.spawn_players()

    #### Events handlers ##############################
    def draw(self):
        for p in self._players:
            p.draw()

    def update(self, dt):
        # Collisions
        for i in range(len(self._players)):
            for j in range(i + 1, len(self._players)):
                collision = self._players[i]._collider.check_collision(self._players[j]._collider)
                if collision:
                    self._players[i]._collider.on_stay(collision)

        # 
        for p in self._players_controllers:
            p.update(dt)

        for p in self._players:
            p.update(dt)

    ###################################################
    #### Game Logic ###################################
    ###################################################
    def spawn_players(self):
        human_players = 1   # Human
        ai_players = 2      # AI

        offset = 50
        x, y = Context.window.width, Context.window.height

        for i in range(human_players):
            new_player = Player("red")
            new_player.set_pos(random.randint(0 + offset, x - offset), random.randint(0 + offset, y - offset))

            new_player_controller = PlayerControllerHuman(new_player)
            self._players.append(new_player)
            self._players_controllers.append(new_player_controller)
            
        for i in range(ai_players):
            new_player = Player("blue")
            new_player.set_pos(random.randint(0 + offset, x - offset), random.randint(0 + offset, y - offset))
            
            new_player_controller = PlayerControllerAI(new_player)
            self._players.append(new_player)
            self._players_controllers.append(new_player_controller)
    