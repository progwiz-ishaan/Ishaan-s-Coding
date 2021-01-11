import random

FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
FINAL_LEVEL = 6
START_SPEED = 10
COLOURS = ['green', 'blue']

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit('space', (0, 0))
    if game_over:
        display_message('GAME OVER!', 'Try again.')
    elif game_complete:
        display_message("YOU WON!", 'Well done.')
    else:
        for star in stars:
            star.draw()

def make_stars():
    colours_to_create = get_colours_to_create(number_of_extra_stars)
    new_stars = create_stars(colours_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colours_to_create(number_of_extra_stars):
    return []

def create_stars(colours_to_create):
    return []

def layout_stars(stars_to_layout):
    pass

def animate_stars(stars_to_animate):
    pass