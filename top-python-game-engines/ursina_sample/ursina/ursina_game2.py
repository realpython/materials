from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


app = Ursina()
anim = Animation('ursina_wink', loop=True, autoplay=False)
a = Animator(
    animations = {
        'lol' : Entity(model='cube', color=color.red),
        'yo' : Entity(model='cube', color=color.green, x=1),
        'help' : anim,
    }
)
a.state = 'yo'

Text('press 1, 2 or 3 to toggle different animator states', origin=(0,-.5), y=-.4)

def input(key):
    if key == '1':
        a.state = 'lol'
    if key == '2':
        a.state = 'yo'
    if key == '3':
        a.state = 'help'
        print(anim.enabled)
        
app.run()