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
    'eggs': Actor('one-egg', pos=(400, 100)),
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

lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor('hero', pos=HERO_START)

def draw():
    global lairs, eggs_collected, lives, game_comlpete
    screen.clear()
    screen.blit('dungeon', (0, 0))
    if game_over:
        screen.draw.text('GAME OVER!', fontsize=60, center=CENTER, color=FONT_COLOUR)
    elif game_comlpete:
        screen.draw.text('YOU WON!', fontsize=60, center=CENTER, color=FONT_COLOUR)
    else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)

def draw_lairs(lairs_to_draw):
    pass

def draw_counters(eggs_collected, lives):
    pass

pgzrun.go()