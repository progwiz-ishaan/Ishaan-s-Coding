import pgzrun
from random import randint
import time

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

game_over = False
finalised = False
garden_happy = True
fangflower_collision = False

time_elasped = 0
start_time = time.time()

cow = Actor('cow')
cow.pos = 100, 500

flower_list = []
wilted_list = []
fangflower_list = []

fangflower_vy_list = []
fangflower_vx_list = []