import constants, json
import re
from bottle import route, run, template, request, static_file
from IPython import embed
from bossafy import Bossafy


def get_structured_chords(chord_data):
    chords = chord_data.keys()
    all_chord_types = set()
    possible_roots = ['Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G' ]
    root_notes = ['Ab', 'Bb', 'C#', 'Db', 'Eb', 'F#', 'Gb' ]
    for root_note in root_notes:
        matching_chords = [ chord for chord in chords if chord.startswith(root_note)]
        [all_chord_types.add(chord[2:]) for chord in matching_chords]

    # dict keys are chord_types, values of each is array of root notes
    # return sorted by number of root notes for corresponsing chord_types
    chords_by_type = {}
    for chord_type in all_chord_types:
        chords_by_type[chord_type] = []
        for chord in chords :
            if chord_type in chord:
                potential_new_chord = chord.replace(chord_type, '')
                if potential_new_chord in possible_roots:
                    chords_by_type[chord_type].append(potential_new_chord)

    return {k: v for k, v in chords_by_type.items() if len(v) == 12}


@route('/')
def index():
     return static_file('index.html', root='./client/')

@route('/next_chord')
def next_chord():
    # return template('gonna look up %s' % (request.query.get('chord')))
    chord, chord_type = request.query.get('chord'), request.query.get('chord_type')
    if not chord_type:
        chord_type = 'chord'
    return Bossafy().get_user_input(chord, chord_type)

@route('/chords')
def chords():
    with open(constants.CHORDS_FILE_PATH, 'r') as chords:
        chord_data = json.load(chords)

        return { "chords": chord_data, "structured_chords": get_structured_chords(chord_data) }

# @route('/structured_chords')
# def structured_chords():
#     with open(constants.CHORDS_FILE_PATH, 'r') as chord_data:
#

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./client/')


run(host='localhost', port=80, reloader=True)
