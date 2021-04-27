# Make a geometric rainbow pattern.
import turtle
shelly = turtle.Turtle()
# pick a order of colours for the hexgon.
colours = ['red', 'yellow', 'blue', 'orange', 'green', 'red']
turtle.bgcolor('black') # turn the background black
# draw 36 hexgons, each 10 degrees apart.
for n in range(36):
# make a hexgon by repeating 6 times.
    for h in range(6):
        shelly.color(colours[h]) # Pick colour at position i.
        shelly.forward(100)
        shelly.left(60)
    # add a turn before the next hexgon.
    shelly.right(10)

# get ready to draw 36 circles.
shelly.penup()
shelly.color('white')
# repeat 36 times to mach the 36 hexons.
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
# hide turtle to finish the drawing.
shelly.hideturtle()
# Prevent the program form qutting by asking the user a question
w = input()