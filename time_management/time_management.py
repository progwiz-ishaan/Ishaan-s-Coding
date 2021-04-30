# The Time Management program:
from tkinter import *
from tkinter.messagebox import showinfo
from datetime import timedelta, datetime
from task import Task
from functions import window_func

# Set up the window.
class Window(Tk):
    """A class to represent a window."""

    def __init__(self):
        """Initialize attributes of a window."""
        super().__init__() # Intitalize all attrubutes from the parent class to the child class.

        # Initialize all the widgets.
        self.welcome = Label(self, text='Welcome back, Deepti!!', width=20, height=5, \
        bg='black', fg='orange', font=("Cursive", 30))

        self.u1i1 = Button(self, text='More Urgent, More Impotant', fg='orange', \
        bg='black', command=lambda text='u1i1' : add_task(text))

        self.u1i0 = Button(self, text="More Urgent, Less Impotant", fg='orange', \
        bg='black', command=lambda text='u1i0' : add_task(text))

        self.u0i1 = Button(self, text='Less Urgent, More Impotant', fg='orange', \
        bg='black', command=lambda text='u0i1' : add_task(text))

        self.u0i0 = Button(self, text="Less Urgent, Less Impotant", fg='orange', \
        bg='black', command=lambda text='u0i0' : add_task(text))

    def run(self):
        """Pack all widegets and start the mainloop."""
        # Pack all widets.
        self.welcome.pack()
        self.u1i1.pack()
        self.u1i0.pack()
        self.u0i1.pack()
        self.u0i0.pack()
        # Start the mainloop.
        self.mainloop()

    def add_task(self, text):
        """Create a new window with the given text."""


if __name__ == '__main__':
    home = Window()
    home.title("Time Manaegment")
    home.configure(bg='black')
    home.run()