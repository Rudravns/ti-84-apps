from ti_draw import *
from random import randint
from ti_system import get_key
from CONSTANT import *

# Player
px = 150
py = 200
pw = 20
ph = 10
speed = 2

# Enemy
ex = randint(0, 310)
ey = 0
ew = 10
eh = 10
enemy_speed = 2

# Initial draw
set_color(0, 0, 255)
fill_rect(px, py, pw, ph)

set_color(255, 0, 0)
fill_rect(ex, ey, ew, eh)

while True:

    # Quit game
    
    if get_key(0) == KEY_CLEAR:
        break

    # Erase old objects
    set_color(255, 255, 255)
    fill_rect(px, py, pw, ph)
    fill_rect(ex, ey, ew, eh)

    # Move player
    key = getKey(0)
    if key == KEY_LEFT:
        px -= speed
    elif key == KEY_RIGHT:
        px += speed

    # Keep player on screen
    if px < 0:
        px = 0
    elif px > 320 - pw:
        px = 320 - pw

    if py < 0:
        py = 0
    elif py > 210 - ph:
        py = 210 - ph

    # Move enemy
    ey += enemy_speed

    # Respawn enemy
    if ey > 210:
        ey = 0
        ex = randint(0, 310)

    # Collision
    if (px < ex + ew and
        px + pw > ex and
        py < ey + eh and
        py + ph > ey):

        clear()
        draw_text(110, 100, "GAME OVER")
        break

    # Draw player
    set_color(0, 0, 255)
    fill_rect(px, py, pw, ph)

    # Draw enemy
    set_color(255, 0, 0)
    fill_rect(ex, ey, ew, eh)