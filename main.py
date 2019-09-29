import pyglet
from pyglet.window import key 
from pyglet.window import FPSDisplay

from engine import utils, context
from engine.scene.scenes_stack import *

from game.scenes.scene_main import *

# Init
window = pyglet.window.Window(width = 1024, height = 720, vsync = False)
fps_display = FPSDisplay(window)

key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)

Context.window = window
Context.key_handler = key_handler
Context.fps_display = True

# Init state stack
main_stack = ScenesStack()
main_stack.push_scene(SceneMain)

# Loop
@window.event
def on_draw():
    window.clear()

    fps_display.draw()
    main_stack.draw()

def update(dt):
    main_stack.update(dt)

pyglet.clock.schedule_interval(update, 1/120.0)

# Run
pyglet.app.run()