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

root.mainloop()