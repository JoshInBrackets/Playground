import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fet', 'red',\
    'orange', 'yellow', 'green', 'blue', 'purple', 'white',\
    'proud', 'brave']

nouns = ['apple', 'dino', 'ball', 'toaster' , 'goat', 'dargon',\
    'hammer', 'duck', 'panda']

print('Welcome to password picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print('Your password is: ' + password)
    response = input('Would you like another password? type y or n\n')
    if response == 'n':
        break