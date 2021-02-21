import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbol(x, y):
    global first
    global previousX, previousY
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True

root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)
buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [u'\2702', u'\2702', u'\2705', u'\2705', u'\2708', u'\2708', u'\2709', u'\2709', u'\270A', u'\270A', \
    u'\270B', u'\270B', u'\270C', u'\270C', u'\270F', u'\270F', u'\27012', u'\27012', u'\27014', u'\27014', \
        u'\27016', u'\27016', u'\27028', u'\27028']
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=3, height=3)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

root.mainloop()