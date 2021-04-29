from tkinter import *
from tkinter.messagebox import showinfo
from task import Task

def add_task(name, task_type, task_time, task_date, task_deadline, task_remind):
    """Add task to its respective file."""
    print(task_time)
    new_task = Task(name, task_type, task_time, task_date, task_deadline, task_remind)
    new_task.append_to_file()
    message = showinfo("Task Added Sucsssfully", "Task added sucsssfully!!!")
    add_task_window.destory()
    message

def window_func(title):
    """Create a new window with buttons and all."""
    title_ = title.split(', ')
    add_task_window = Tk()
    add_task_window.title("Add Task")
    add_task_window.configure(bg='black')
    # Entries
    name = Entry(add_task_window, fg='orange', bg='black')
    time = Entry(add_task_window, fg='orange', bg='black')
    date = Entry(add_task_window, fg='orange', bg='black')
    deadline = Entry(add_task_window, fg='orange', bg='black')
    remind = Entry(add_task_window, fg='orange', bg='black')
    name.pack()
    time.pack()
    date.pack()
    deadline.pack()
    remind.pack()

    # Buttons
    add_task_ = Button(add_task_window, text='Add Task', fg='orange', bg='black'\
    , command=lambda n=name.get(), ty=title_[1], ti=time.get(), da=date.get(), de=deadline.get(), r=remind.get()\
     : add_task(n, ty, ti, da, de, r))
    add_task_.pack()