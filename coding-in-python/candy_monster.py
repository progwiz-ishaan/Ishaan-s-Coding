# The Candy Monster Game program:
from tkinter import *
import random

# Window
# make window
window = Tk()
window.title("The Candy Monster Game")

# create a canvas to put objects on the screen
canvas = Canvas(window, width=400, height=400, bg='black')
canvas.pack()

# Welcome Screen
# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text='The Candy Monster',\
 fill='white', font=('Helvetica', 30))
directions = canvas.create_text(200, 300, text='Collect Candy but no red ones\
', fill='white', font=('Helvetica', 20))

# set up score display using label wiget
score = 0
score_display = Label(window, text='Score: ' + str(score))
score_display.pack()

# set up level display using label wiget
level = 1
level_display = Label(window, text='Level: ' + str(level))
level_display.pack()

# create an image object using the .gif file
player_image = PhotoImage(file='/home/ishaan/Documents/Ishaan\'s-Coding/coding\
-in-python/greenChar.gif')
# use image object to create a character at position 200, 360
my_char = canvas.create_image(200, 360, image=player_image)

# Candy
# variables and lists needed for manging candy.
candy_list = [] # list containing all candy created, empty at start.
bad_candy_list = [] # list containing all bad candy created, empty at start.
candy_speed = 2 # initial speed for all falling candy
candy_colour_list = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'whit\
e']

# function to make candy at random places
def make_candy():
    # pick a random x position
    xposition = random.randint(1, 400)
    # pick a random colour
    candy_colour = random.choice(candy_colour_list)
    # create candy the size of 30 at random position and colour
    candy = canvas.create_oval(xposition, 0, xposition+30, 30, fill=candy_colour)
    # add candy to list
    candy_list.append(candy)
    # if candy colour is red - add it to bad candy list
    if candy_colour == 'red':
        bad_candy_list.append(candy)
        #

window.mainloop() # last line is the GUI main event loop