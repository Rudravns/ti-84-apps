from ti_system import *
from CONSTANT import *

def move_player(x, y, speed):
    key = get_key(0)

    if key == KEY_LEFT:
        x -= speed
    elif key == KEY_RIGHT:
        x += speed
    elif key == KEY_UP:
        y -= speed
    elif key == KEY_DOWN:
        y += speed

    return x, y

if __name__ == "__main__":
    while True:
        print(wait_key())
        =