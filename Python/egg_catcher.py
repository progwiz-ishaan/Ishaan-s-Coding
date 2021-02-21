from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400

root = Tk()
c = Canvas(root, width=canvas_width, height=canvas_height, bg='deep sky blue')
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

colour_cycle = cycle(['light blue', 'light cyan', 'light pink', 'light yellow', 'light green'])
egg_width = 45
egg_height = 45
egg_score = 10
egg_speed = 500
egg_interval = 4000
diffulty_factor = 0.95

root.mainloop()