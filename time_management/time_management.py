# The Time Management program:
from tkinter import *
from tkinter.messagebox import showinfo
from datetime import timedelta, datetime
from task import Task
from functions import window_func

# Set up the window.
window = Tk()
window.title("Time Management for Deepti")
window.configure(bg='black', width=400, height=400)

# Set up the widgets.
welcome = Label(window, text='Welcome back, Deepti!!', width=20, height=5, \
bg='black', fg='orange', font=("Cursive", 30))
welcome.pack()

u1i1 = Button(window, text='More Urgent, More Impotant', fg='orange', \
bg='black', command=lambda s='More Urgent, More Impotant, u1i1' : window_func(s))
u1i1.pack()

u1i0 = Button(window, text="More Urgent, Less Impotant", fg='orange', \
bg='black', command=lambda s='More Urgent, Less Impotant, u1i0' : window_func(s))
u1i0.pack()

u0i1 = Button(window, text='Less Urgent, More Impotant', fg='orange', \
bg='black', command=lambda s='Less Urgent, More Impotant, u0i1' : window_func(s))
u0i1.pack()

u0i0 = Button(window, text="Less Urgent, Less Impotant", fg='orange', \
bg='black', command=lambda s='Less Urgent, Less Impotant, u0i0' : window_func(s))
u0i0.pack()

window.mainloop()