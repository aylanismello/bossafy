from IPython import embed
import json
import pprint
import sys
import operator


try:
    artist_name = sys.argv[1]
except IndexError as err:
    print(f"You need to pass an artist name!")
    exit()

with open(f"./{artist_name}_chords.json") as data_file:
    data = json.load(data_file)

# only get the 'chords' list value within each chord dictionary/json hash
all_chords = [song['chords'] for song in data]
non_empty_chords = [chord for chord in all_chords if chord]
# all_chords = list(map(lambda song: song['chords'], data))
# non_empty_chords = list(filter(lambda chord: chord, all_chords))

chord_count = {}


for chords in non_empty_chords:
    for chord in chords:
        if chord in chord_count.keys():
            chord_count[chord] += 1
        else:
            chord_count[chord] = 1


# sorted_chord_count = list(reverse(sorted(chord_count.items(), key=operator.itemgetter(1))))
sorted_chord_count = sorted(chord_count.items(), key=operator.itemgetter(1))[::-1]
print(sorted_chord_count)
# for chord in final_chords: print(chord)

# print(f"There are a total of {len(final_chords)} unique chords from {artist_name}")
# print len(final_chords)
