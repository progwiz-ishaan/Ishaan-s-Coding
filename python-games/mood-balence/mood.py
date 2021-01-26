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
from time import sleep

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
loop_number = 0
going = True

# This is the face's variable
face = Actor('sad-face', pos=CENTER)

# This function performs the first step.
def draw():
    global going
    face.draw()
    screen.draw.text(
        'Face.no: ' + 
        str(face_count),
        color=(65, 105, 225),
        topleft=(10, 10)
    )
    loop()

# This function loop through the faces.
def loop():
    global face_count, loop_number, going
    loop_number += 1
    if face.image == 'sad-face':
        sleep(1)
    elif face.image == 'sad-face1':
         sleep(1)
        face.image = 'sad-face2'
        face_count += 1
    elif face.image == 'sad-face2':
        sleep(1)
        face.image = 'sad-face3'
        face_count += 1
    elif face.image == 'sad-face3':
        sleep(1)
        face.image = 'sad-face4'
        face_count += 1

pgzrun.go()