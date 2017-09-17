from IPython import embed
import json
import pprint
import sys
import operator

from treat_chords import chord_to_relative, relative_to_chord

try:
    artist_name = sys.argv[1]
except IndexError as err:
    print("You need to pass an artist name!")
    exit()

with open("./scraped_" + artist_name + "_chords.json") as data_file:
    scraped_data = json.load(data_file)

# only get the 'chords' list value within each chord dictionary/json hash
songs = [song for song in scraped_data if song['chords'] and song['key']]

with open('./relative_chord_corpus.txt', 'w') as data_file:
    for song in songs:
        for chord in song['chords']:

            # CHECK IF chord_to_relative is really an inverse of relative_to_chord

            chord = chord.replace('\xb0', 'dim')
            chord = chord.replace('\xba', 'dim')
            # data_file.write(chord_to_relative(chord, song['key']) + '\n')
            relative_chord = chord_to_relative(chord, song['key'])
            if(relative_chord != relative_to_chord(relative_chord, song['key'])):
                embed()
            data_file.write(relative_chord + ' ')
        data_file.write('. ')
