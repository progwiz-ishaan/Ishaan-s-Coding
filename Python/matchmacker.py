from random import shuffle
from time import sleep
from tkinter import Tk, Button, DISABLED

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

root.mainloop()