import random
import string

adjectives = [
    'sleepy', 'strong', 'smelly',
    'dirty', 'wet', 'fat', 'thin',
    'red', 'orange', 'yellow', 'sleepy',
    'green', 'pink', 'blue', 'black',
    'purple', 'white', 'proud', 'brave',
    'dry']

nouns = [
    'apple', 'orange', 'banana',
    'goat', 'duck', 'man', 'goose',
    'computer', 'panda', 'dinosaur',
    'hammer', 'toster', 'mouse', 'tiger',
    'ball', 'dragon', 'mango', 'wizard']

print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    num = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(num) + special_char
    print('Your new password is: ' + password)

    response = input('Do you want another password?(y, n): ')
    if response == 'n':
        break
