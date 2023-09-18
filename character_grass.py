from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    x = 0
    while (x < 800):
    
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90
    while (y < 600):
    
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800,y)
        y = y + 2
        delay(0.01)

    x2 = 800
    while (x2 > 0):
    
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x2, 600)
        x2 = x2 - 2
        delay(0.01)
    
    y2 = 600
    while (y2 > 90):
    
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0,y2)
        y2 = y2 - 2
        delay(0.01)

close_canvas()

