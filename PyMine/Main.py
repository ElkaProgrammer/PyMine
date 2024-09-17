from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

app = Ursina(title='ursina', icon='textures/ursina.ico', borderless=False, fullscreen=False, size=("800", "600"), forced_aspect_ratio=None, position=None, vsync=False, editor_ui_enabled=False, window_type='onscreen', development_mode=False, render_mode=None, show_ursina_splash=False)
player = FirstPersonController(speed = 7)
Sky(texture='Sky.png')
punch_sound = Audio('place.mp3',loop = False, autoplay = False)
grass = load_texture('grass.jpg')

boxes = []
for i in range(20):
  for j in range(20):
    box = Button(color=color.white, model='cube', position=(j,0,i),
    texture='grass.jpg', parent=scene, origin_y=0.5, shader = basic_lighting_shader)
    boxes.append(box)

def input(key):

  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        punch_sound.play()
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture=grass, parent=scene, origin_y=0.5,shader = basic_lighting_shader)
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)
    if key == 'p':
        exit(1)

app.run()
