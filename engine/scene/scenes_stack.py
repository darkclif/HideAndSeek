class ScenesStack():
    ###################################################
    ##### Methods #####################################
    ###################################################
    def __init__(self):
        self._stack = []

        self._to_pop = []
        self._to_push = []

    #### Handle stack #################################
    def is_empty(self):
        return not len(self._stack)

    def push_scene(self, scene_class, *args):
        self._to_push.append(scene_class(self, *args))

    def pop_scene(self, scene):
        self._to_pop.append(scene)

    def _pop_scene_execute(self):
        for s in self._to_pop:
            self._stack.remove(s)

        self._to_pop = []

    def _push_scene_execute(self):
        self._stack.extend(self._to_push)
        self._to_push = []

    #### Update / Draw ################################
    def update(self, dt):
        # Update all states from top downward
        for state in reversed(self._stack):
            if (state._force_update) or (state == self._stack[-1]):
                state.update(dt)
        
        # Pop and push queued states
        self._pop_scene_execute()
        self._push_scene_execute()

    def draw(self):
        for state in reversed(self._stack):
            if (state._force_draw) or (state == self._stack[-1]):
                state.draw()
