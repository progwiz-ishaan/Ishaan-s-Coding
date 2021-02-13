import turtle as t

def draw_circle(size):
    t.pencolor('red')
    t.circle(size)
    draw_circle(size)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
draw_circle(30)

keep_going_var = input()