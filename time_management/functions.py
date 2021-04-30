from tkinter import *
from tkinter.messagebox import showinfo
from task import Task

class Add_task(Tk):
    """A class to create a new add task window."""

    def __init__(self, mode):
        """Initialize attributes of a "Add task" window."""
        super().__init__() # Initialize attributes from the parent class to the child class.
        self.mode = mode
        self.name = Entry(self, fg='orange', bg='black')
        self.time = Entry(self, fg='orange', bg='black')
        self.date = Entry(self, fg='orange', bg='black')
        self.deadline = Entry(self, fg='orange', bg='black')
        self.remind = Entry(self, fg='orange', bg='black')
        self.add_task_ = Button(add_task_window, text='Add Task', fg='orange', bg='black')

def add_task(name, task_type, task_time, task_date, task_deadline, task_remind, s):
    """Add task to its respective file."""
    print(s)
    if False:
        new_task = Task(name, task_type, task_time, task_date, task_deadline, task_remind)
        new_task.append_to_file()
        message = showinfo("Task Added Sucsssfully", "Task added sucsssfully!!!")
        add_task_window.destory()

def window_func(title):
    """Create a new window with buttons and all."""
    title_ = title.split(', ')
    add_task_window = Tk()
    add_task_window.title("Add Task")
    add_task_window.configure(bg='black')
    # Entries
    s = StringVar()
    name = 
    time = 
    date = 
    deadline = 
    remind = 
    name.pack()
    time.pack()
    date.pack()
    deadline.pack()
    remind.pack()

    # Buttons
    
    add_task_.pack()
    print(s.get())