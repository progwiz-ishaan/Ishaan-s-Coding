import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor('dancer-start')
dancer.pos = CENTER_X + 5, CENTER_Y - 40

up = Actor('up')
up.pos = CENTER_X, CENTER_Y + 110
right = Actor('right')
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor('down')
down.pos = CENTER_X, CENTER_Y + 230
left = Actor('left')
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit('stage', (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        left.draw()
        right.draw()
        screen.draw.text('Score: ' +
                         str(score), color='black',
                         topleft=(10, 10))
    return

def reset_dancer():
    pass

def update_dancer(move):
    pass

def display_moves():
    pass

def genrate_moves():
    pass

def countdown():
    pass

def next_move():
    pass

def on_key_up(key):
    pass

def update():
    pass

pgzrun.go() 