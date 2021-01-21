############################################################
## 1. A face is drawn and at the topleft corner the face number is drawn.
## If the player presses [DOWN] the face gets more sad.
## If the player presses [UP] the face gets more happy.
## The goal of the game if to make the face's mood good.
## The player has to press the [ENTER] key when he/she thinks the the mood is normal.
## If the face is too happy or sad then it's game over.
############################################################
import pgzrun
from random import randint

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

# This function checks if the [UP] key is pressed.
def update():
        if face.image == 'sad-face' and keyboard.up:
            face.image = 'sad-face1'
        elif face.image == 'sad-face1' and keyboard.up:
            face.image = 'sad-face2'
        elif face.image == 'sad-face2' and keyboard.up:
            face.image = 'sad-face3'

pgzrun.go()