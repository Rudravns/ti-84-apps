from ti_draw import *
from random import randint
from ti_system import getKey
from CONSTANT import *

# ======================
# Settings
# ======================
cell = 10
width = 32
height = 21

# Snake starts in center
snake = [[16, 10]]
dx, dy = 1, 0

# Food
food = [randint(0, width-1), randint(0, height-1)]

# ======================
# Game loop
# ======================
while True:

    key = getKey(0)

    # Quit
    if key == KEY_CLEAR:
        break

    # ======================
    # Direction control
    # ======================
    if key == KEY_LEFT and dx != 1:
        dx, dy = -1, 0
    elif key == KEY_RIGHT and dx != -1:
        dx, dy = 1, 0
    elif key == KEY_UP and dy != 1:
        dx, dy = 0, -1
    elif key == KEY_DOWN and dy != -1:
        dx, dy = 0, 1

    # ======================
    # Move snake
    # ======================
    head = snake[0][:]
    head[0] += dx
    head[1] += dy

    snake.insert(0, head)

    # ======================
    # Food check
    # ======================
    if head == food:
        food = [randint(0, width-1), randint(0, height-1)]
    else:
        snake.pop()

    # ======================
    # Collision (walls)
    # ======================
    if (head[0] < 0 or head[0] >= width or
        head[1] < 0 or head[1] >= height):
        break

    # Collision (self)
    if head in snake[1:]:
        break

    # ======================
    # DRAW
    # ======================
    clear()

    # Food
    set_color(255, 0, 0)
    fill_rect(food[0]*cell, food[1]*cell, cell, cell)

    # Snake
    set_color(0, 0, 255)
    for part in snake:
        fill_rect(part[0]*cell, part[1]*cell, cell, cell)

# ======================
# Game over screen
# ======================
clear()
draw_text(90, 100, "GAME OVER")
print("Score:", len(snake) - 1)