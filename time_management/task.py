from datetime import datetime, timedelta

class Task():
    """A class to represent a task given by the user."""

    def __init__(self, name, task_type, task_time, task_date, task_deadline, task_remind):
        """Initialize attributes of a task."""
        self.name = name
        self.task_type = task_type
        self.task_time = datetime.strptime(task_time, "%H:%M")
        self.task_date = datetime.strptime(task_date, "%d/%m/%Y")
        self.remind = self.deadline - timedelta(days=task_remind)
        self.deadline = datetime.strptime(task_deadline, "%d/%m/%Y")

    def append_to_file(self):
        """Append the task to it's respective .txt file."""
        filename = f"/home/ishaan/Documents/Ishaan's-Coding/time_management/{self.task_type}.txt"
        with open(filename, 'a') as f:
            f.write(f"{self.name} : {str(self.task_date)} : {str(self.task_time)} : {str(self.deadline)}\
             : {str(self.remind)}\n")