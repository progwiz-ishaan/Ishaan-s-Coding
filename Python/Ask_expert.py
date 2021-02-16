from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
def write_to_file(country_name, city_name):
    with open('capital_data.txt') as file:
        file.write('\n' + country_name + '/' + city_name)
root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of the country:')

    if query_country in the_world[query_country]:
        result = the