from tkinter import Tk, Canvas
from datetime import date, datetime
def get_events():
    list_events = []
    with  open('events.txt')
root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange',\
    font='Arial 28 bold underline', text='My Countdown Calender')

root.mainloop()