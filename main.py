import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

image = pyglet.resource.image('Assets/kitten.jpg')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(x,y)

@window.event
def on_key_press(symbol, modifiers):
    window.clear()
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()
    
pyglet.app.run()