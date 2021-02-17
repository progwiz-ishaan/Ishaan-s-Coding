from tkinter import simpledialog, messagebox, Tk
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        messagebox.showinfo('Message to encrypt is:', message)
    if task == 'decrypt':
        message = get_message()
        messagebox.showinfo('Message to decrypt is:', message)