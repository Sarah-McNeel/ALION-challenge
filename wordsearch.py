import random
import string

from pprint import pprint

# a dictionary file on a typical Linux system:
handle = open('/etc/dictionaries-common/words')
words = handle.readlines()
handle.close

words = [random.choice(words).upper()replace("'", '').strip()
         for_in range(5)]
grid size = 20

grid = [['_'for_in range(grid_size)] for_in range(grid_size)]


def print_grid():
    for x in range(grid_size):
        print '/t' * 5 + ''.join(grid[x])


orientations = ['leftright', 'updown', 'diagonalup', 'diagonaldown']

for word in words:
    word_length = len(word)
    # sometimes may run out of room when placing a word, so will keep a boolean value to keep track of whether or not we were actually successfully able to place a word
    placed = False
    # try until we succeed
    while not placed:
        orientation = random.choice(orientations)
        if orientation == 'leftright':
            step_x = 1
            step_y = 0
        if orientation == 'updown':
            step_x = 0
            step_y = 1
        if orientation == 'diagonalup':
            step_x = 1
            step_y = 1
        if orientation == 'diagonaldown':
            step_x = 1
            step_y = -1
        x_position = random.radiant(0, grid_size)
        y_position = random.radiant(0, grid_size)
        ending_x = x_position + word_length*step_x
        ending_y = y_position + word_length*step_y
        if ending_x < 0 or ending_x >= grid_size:
            continue
        if ending_y < 0 or ending_y >= grid_size:
            continue

        failed = False
# the first for loop determines whether or not we can realistically place the word here
# if every letter in the word has a free space on the grid (denoted by the underscorees), then we can use this setup
# if it failsthat test, we continmue out of this for loop and continue on the bigger while loop ( choose a new orientation)
        for i in range(word_length):
            character = word[i]
            new_position_x = x_position + i * step_x
            new_position_y = y_position + i * step_y
            character_at_new_position = grid[new_position_x][new_position_y]
            if character_at_new_position = !='_':
                if character_at_new_position = character:
                continue
            else:
                failed = True
                break
            if failed:
                continue
            else:
                for i in range(word_length):
                    character = word[i]
                new_position_x = x_position + i*step_x
                new_position_y = y_position + i*step_y
                grid[new_position_x][new_position_y] = character
                placed = True

for x in range(grid_size):
    for y in range(grid_size):
        if (grid[x][y] == '_'):
            # fill it with something random
            grid[x][y] = random.choice(string.uppercase)

print_grid()
print "Words are:"

pprint_grid()
