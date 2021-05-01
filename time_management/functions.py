from tkinter import Tk, Entry, Button
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
        self.add_task_ = Button(self, text='Add Task', fg='orange', bg='black', command=self.add_task)
        self.convert_to_title()

    def convert_to_title(self):
        """Convert the given code to plaintext."""
        self.converted_code = ''
        if self.mode[:1] == '1':
            self.converted_code += 'MU'
        else:
            self.converted_code += 'LU'
        if self.mode[:3] == '1':
            self.converted_code += 'MI'
        else:
            self.converted_code += 'LI'

    def add_task(self):
        """Add task to its respective file."""
        new_task = Task(self.name.get(), self.mode, self.time.get(), self.date.get(), self.deadline.get(), self.remind.get())
        new_task.append_to_file()

    def run(self):
        """Create the window."""
        self.name.pack()
        self.date.pack()
        self.time.pack()
        self.deadline.pack()
        self.remind.pack()
        self.add_task_.pack()

        self.title(f"Add task {self.converted_code}")
        self.configure(bg='black')
        self.mainloop()