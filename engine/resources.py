import pyglet
from engine.utils import *

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

pawn_1_image = pyglet.resource.image("pawn_1.png")
pawn_2_image = pyglet.resource.image("pawn_2.png")

center_image_anchor(pawn_1_image)
center_image_anchor(pawn_2_image)