# The Time Management program:
from tkinter import *
from tkinter.messagebox import showinfo

# Classes
class Task():
    """A class to represent a task given by the user."""

    def __init__(self, name, task_type):
        """Initialize attributes of a task."""
        self.name = name
        self.task_type = task_type