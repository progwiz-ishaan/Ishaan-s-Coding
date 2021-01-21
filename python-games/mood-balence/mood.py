############################################################
## 1. A face is drawn and at the topleft corner the face number is drawn.
## Each second, the face changes to more happy and then when it reaches the limit it reverses back to sad each
## second.
## The goal of the game is to press the [ENTER] key when the player thinks that the current face is the nor-
## -mal face. 
## If the face is too happy or sad then it's game over.
############################################################
import pgzrun
from random import randint
import time

# The consonants
WIDTH = 400
HEIGHT = 400
CENTER_X = WIDTH / 2
CENTER_Y = WIDTH / 2
CENTER = (CENTER_X, CENTER_Y)
HAPPY_FACES_NEEDED = randint(2, 5)

# The global variables
game_over = False
game_complete = False
face_count = 0

# This is the face's variable
face = Actor('sad-face', pos=CENTER)

# This function performs the first step.
def draw():
    screen.clear()
    face.draw()
    screen.draw.text(
        'Face.no: ' + 
        str(face_count),
        color=(65, 105, 225),
        topleft=(10, 10)
    )

# This function loop through the faces.
def loop():
    scren.draw.text('GO!!', color=(65, 105, 225),
    center=(CENTER_X, CENTER_Y - 50))


pgzrun.go()