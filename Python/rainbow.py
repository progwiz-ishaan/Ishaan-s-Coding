import random as r
import turtle as t

def get_line_length():
    choice = input ('Enter line length (long, medium, short): ')
    if choice == 'long':
        line_length = 250
    elif choice == 'meidum':
        line_length = 200
    else:
        line_length = 100
    return line_length

def get_line_width():
    choice = input ('Enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 25
    else:
        line_width = 10
    return line_width

line_length = get_line_length ()
line_width = get_line_width ()