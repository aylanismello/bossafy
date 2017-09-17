import random, sys, json
from collections import defaultdict
from treat_chords import chord_to_relative, relative_to_chord


try:
    KEY = sys.argv[1]
except IndexError as err:
    print("Did not pass key, defaulting to F")
    KEY = 'F'

KEY = KEY.upper()

with open('./data/chord_corpus.txt') as chords:
    CORPUS = chords.read().split(' ')

prev_chord = '.'
distribution = defaultdict(list)
for chord in CORPUS:
    # simply ! is 3
    if len(chord) <= 3:
        distribution[prev_chord].append(chord)
        prev_chord = chord

def print_chord_vertically(chord):
    for note in chord.split(' '):
        print(note)

def next_chord(chord, key):
    """Get next chord"""
    relative_chord = chord_to_relative(chord, key)
    # if relative_chord not in distribution.keys():
    if relative_chord in list(distribution.keys()):
        next_relative_chord = random.choice(distribution[relative_chord])
        return relative_to_chord(next_relative_chord, key)
    else:
        return '.'

try:
    with open('./data/chord_dict.json', 'r') as file_data:
        chord_dict = json.load(file_data)
except:
    print('could not open chord dictionary, failing')
    exit()

current_chord = '.'
while True:
    current_chord = next_chord(current_chord, KEY)
    if current_chord == '.':
        break
    if current_chord not in list(chord_dict.keys()):
        print(current_chord + ' not in dict!!')
        continue
    print(current_chord + ': ')
    print_chord_vertically(chord_dict[current_chord])
    print('\n\n')
