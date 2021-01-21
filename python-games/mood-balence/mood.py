import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
CENTER_X = WIDTH / 2
CENTER_Y = WIDTH / 2
CENTER = (CENTER_X, CENTER_Y)
HAPPY_FACES_NEEDED = randint(2, 5)

game_over = False
game_complete = False
face_count = 0

face = Actor('sad-face', pos=CENTER)

def draw():
    screen.clear()
    face.draw()
    screen.draw.text(
        'Face.no: ' + 
        str(face_count),
        color=(0, 0, 0),
        topleft=(10, 10)
    )

pgzrun.go()