import random

lives = 9
words = ['shirt', 'human', 'fairy', 'teeth', 'otter', 'plane', 'eight', 'pizza', 'lives']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    for char in secret_word:
        if guessed_letter == char:
            clue[index] = char
        index += 1

print(heart_symbol)