from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

app = Ursina()
player = FirstPersonController()
Sky()
punch_sound = Audio('place.mp3',loop = False, autoplay = False)
grass = load_texture('grass.jpg')

boxes = []
for i in range(30):
  for j in range(30):
    box = Button(color=color.white, model='cube', position=(j,0,i),
    texture='grass.png', parent=scene, origin_y=0.5, shader = basic_lighting_shader)
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