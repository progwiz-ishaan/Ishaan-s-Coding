import pgzrun
import math

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOUR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (200, 300)
ATTACK_DISTANCE = 200
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 3
eggs_collected = 0
game_over = False
game_comlpete = False
reset_required = False

easy_lair = {
    'dragon': Actor('dragon-asleep', pos=(600, 100)),
    'eggs': Actor('one-eggs', pos=(400, 100)),
    'egg_count': 1,
    'egg_hidden': False,
    'egg_hide_counter': 0,
    'sleep_length': 10,
    'sleep_counter': 0,
    'wake_counter': 0
}

medium_lair = {
    'dragon': Actor('dragon-asleep', pos=(600, 300)),
    'eggs': Actor('two-eggs', pos=(400, 300)),
    'egg_count': 2,
    'egg_hidden': False,
    'egg_hide_counter': 0,
    'sleep_length': 7,
    'sleep_counter': 0,
    'wake_counter': 0
}

hard_lair = {
    'dragon': Actor('dragon-asleep', pos=(600, 500)),
    'eggs': Actor('three-eggs', pos=(400, 500)),
    'egg_count': 3,
    'egg_hidden': False,
    'egg_hide_counter': 0,
    'sleep_length': 4,
    'sleep_counter': 0,
    'wake_counter': 0
}


pgzrun.go()