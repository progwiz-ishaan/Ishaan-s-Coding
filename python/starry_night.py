import turtle as t
from random import randint, random

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# Main code
t.hideturtle()
t.speed('fast')
t.Screen().bgcolor('dark blue')

while True:
    randPts = randint(2, 5) * 2 + 1
    randSize = randint(10, 50)
    randCol = (random(), random(), random())
    randX = randint(-350, 350)
    randY = randint(-250, 250)

    draw_star(randPts, randSize, randCol, randX, randY)