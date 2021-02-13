import turtle

def rectangle(horizontal, vertical, color):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color)
    turtle.begin_fill()
    for counter in range(1, 3):
        turtle.forward(horizontal)
        turtle.right(90)
        turtle.forward(vertical)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

turtle.penup()
turtle.speed('slow')
turtle.bgcolor('Doger blue')

# feet
turtle.goto(-100, -150)
rectangle(50, 20, 'blue')
turtle.goto(-30, -150)
rectangle(50, 20, 'blue')
