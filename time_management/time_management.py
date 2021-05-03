# The Time Management program:
from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo
from datetime import datetime
from task import Task
from add_task import Add_task

class Window(Tk):
    """A class to represent a window."""

    def __init__(self):
        """Initialize attributes of a window."""
        super().__init__() # Intitalize all attrubutes from the parent class to the child class.

        # Initialize all the widgets.
        self.welcome = Label(self, text='Welcome back, Deepti!!', width=20, height=5, \
        bg='black', fg='orange', font=("Cursive", 30))

        self.u1i1 = Button(self, text='Most Urgent, Most Impotant', fg='orange', \
        bg='black', command=lambda text='u1i1' : self.add_task(text))

        self.u1i0 = Button(self, text="Most Urgent, Less Impotant", fg='orange', \
        bg='black', command=lambda text='u1i0' : self.add_task(text))

        self.u0i1 = Button(self, text='Less Urgent, Most Impotant', fg='orange', \
        bg='black', command=lambda text='u0i1' : self.add_task(text))

        self.u0i0 = Button(self, text="Less Urgent, Less Impotant", fg='orange', \
        bg='black', command=lambda text='u0i0' : self.add_task(text))

        self.mode_list = ['u1i1', 'u0i0', 'u1i0', 'u0i1']

    def run(self):
        """Pack all widegets and start the mainloop."""
        # Pack all widets.
        self.welcome.pack()
        self.u1i1.pack()
        self.u1i0.pack()
        self.u0i1.pack()
        self.u0i0.pack()
        # Start the mainloop.
        self.title("Time Management")
        self.configure(bg='black')
        self.mainloop()

    def add_task(self, text):
        """Create a new window with the given text."""
        ad = Add_task(text)
        ad.run()

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

    def check_for_tasks(self):
        """Check for to-do tasks."""
        today = datetime.now()
        for mode in self.mode_list:
            filename = f'/home/ishaan/Documents/Ishaan\'s-Coding/time_management/{mode}.txt'
            with open(filename) as file:
                for line in file:
                    line_list = line.split(' : ')
                    date_str = line_list[1]
                    date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M")%d/%m/%Y %H:%M

if __name__ == '__main__':
    home = Window()
    home.run()