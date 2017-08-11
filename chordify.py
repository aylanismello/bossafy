from IPython import embed
import json
import pprint
import sys
import operator

from treat_chords import chord_to_relative

try:
    artist_name = sys.argv[1]
except IndexError as err:
    print("You need to pass an artist name!")
    exit()



with open("./" + artist_name + "_chords.json") as data_file:
    data = json.load(data_file)

# only get the 'chords' list value within each chord dictionary/json hash
songs = [song for song in data if song['chords'] and song['key']]


# { key: 'fdfd', chords: ['...']}
for song in songs:
    for chord in song['chords']:
        print chord_to_relative(chord, song['key'])
