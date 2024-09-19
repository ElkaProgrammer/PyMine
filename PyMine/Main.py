from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from perlin_noise import PerlinNoise
import random

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))

app = Ursina(title='PyMine', icon='ico.ico', borderless=False, fullscreen=False, size=("800", "600"), forced_aspect_ratio=None, position=None, vsync=False, editor_ui_enabled=False, window_type='onscreen', development_mode=False, render_mode=None, show_ursina_splash=False)
player = FirstPersonController(speed = 6)
Sky()
punch_sound = Audio('place.mp3',loop = False, autoplay = False)
grass = load_texture('grass.jpg')

boxes = []
for i in range(20):
  for j in range(20):
    height = noise([i * 0.02, j * 0.02])
    height = math.floor(height * 7.5)
    box = Button(color=color.white, model='cube', position=(j,height,i),
    texture=grass, parent=scene, origin_y=0.5, shader = basic_lighting_shader)
    boxes.append(box)

def input(key):
  if key == 'p':
    exit(1)

  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
          punch_sound.play()
          new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
          texture="wood.jpg", parent=scene, origin_y=0.5, shader=basic_lighting_shader)
          boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

app.run()

