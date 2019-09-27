class Scene():
    ###################################################
    ##### Methods #####################################
    ###################################################
    def __init__(self, scenes_stack):
        self._scenes_stack = scenes_stack  # Scenes state machine

        self._force_draw = False      # Draw when not on the top of state stack 
        self._force_update = False    # Update when not on the top of state stack

    #### Scene setup ##################################
    def _setup(self):
        pass # To implement in child clases

    #### State machine handler ########################
    def _pop_scene(self):
        self._scenes_stack.pop_scene(self)

    def _push_scene(self, scene):
        self._scenes_stack.push_scene(scene)

    #### Events handlers ##############################
    def draw(self):
        pass

    def update(self):
        pass
