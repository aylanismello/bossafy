import random, sys
from IPython import embed
from collections import defaultdict

from treat_chords import chord_to_relative, relative_to_chord


try:
    KEY = sys.argv[1]
except IndexError as err:
    print "Did not pass key, defaulting to F"
    KEY = 'F'

KEY = KEY.upper()

with open('./chord_corpus.txt') as chords:
    CORPUS = chords.read().split(' ')

prev_chord = '.'
distribution = defaultdict(list)
for chord in CORPUS:
    # simply ! is 3
    if len(chord) <= 3:
        distribution[prev_chord].append(chord)
        prev_chord = chord


def next_chord(chord, key):
    """Get next chord"""
    relative_chord = chord_to_relative(chord, key)
    # if relative_chord not in distribution.keys():
    if relative_chord in distribution.keys():
        next_relative_chord = random.choice(distribution[relative_chord])
        return relative_to_chord(next_relative_chord, key)
    else:
        return '.'

current_chord = '.'
while True:
    current_chord = next_chord(current_chord, KEY)
    print current_chord
    if current_chord == '.':
        break
