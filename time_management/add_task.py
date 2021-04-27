from tkinter import *

def window():
    """Do all things related to the window."""
    add_task_window = Tk()
    add_task_window.title("Add Task")
    add_task_window.configure(bg='black')

def widgets():
    """Do all the things related to widgets."""
    # Entries
    name = Entry(add_task_window, fg='orange', bg='black')
    date = Entry(add_task_window, fg='orange', bg='black')
    time = Entry(add_task_window, fg='orange', bg='black')
    deadline = Entry(add_task_window, fg='orange', bg='black')
    remind = Entry(add_task_window, fg='orange', bg='black')
    name.pack()
    date.pack()
    time.pack()
    deadline.pack()
    remind.pack()