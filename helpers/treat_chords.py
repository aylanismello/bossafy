from mingus.core import progressions

def chord_root_to_scale_degree(root, key):
    return progressions.determine([root], key, True)[0].replace('i', 'I').replace('v', 'V')

def scale_degree_to_chord_root(degree, key):
    return progressions.to_chords([degree], key)[0][0]

def chord_to_relative(chord, key):
    """ accepts a normal chord and a key, returns a normal chord"""
    return chord.replace('A#', chord_root_to_scale_degree('A#', key)) \
                .replace('Ab', chord_root_to_scale_degree('Ab', key)) \
                .replace('A', chord_root_to_scale_degree('A', key)) \
                .replace('B#', chord_root_to_scale_degree('B#', key)) \
                .replace('Bb', chord_root_to_scale_degree('Bb', key)) \
                .replace('B', chord_root_to_scale_degree('B', key)) \
                .replace('C#', chord_root_to_scale_degree('C#', key)) \
                .replace('Cb', chord_root_to_scale_degree('Cb', key)) \
                .replace('C', chord_root_to_scale_degree('C', key)) \
                .replace('D#', chord_root_to_scale_degree('D#', key)) \
                .replace('Db', chord_root_to_scale_degree('Db', key)) \
                .replace('D', chord_root_to_scale_degree('D', key)) \
                .replace('E#', chord_root_to_scale_degree('E#', key)) \
                .replace('Eb', chord_root_to_scale_degree('Eb', key)) \
                .replace('E', chord_root_to_scale_degree('E', key)) \
                .replace('F#', chord_root_to_scale_degree('F#', key)) \
                .replace('Fb', chord_root_to_scale_degree('Fb', key)) \
                .replace('F', chord_root_to_scale_degree('F', key)) \
                .replace('G#', chord_root_to_scale_degree('G#', key)) \
                .replace('Gb', chord_root_to_scale_degree('Gb', key)) \
                .replace('G', chord_root_to_scale_degree('G', key))

def relative_to_chord(chord, key):
    """ accepts a relative chord and a key, returns a normal chord """
    return chord.replace('bVII', scale_degree_to_chord_root('bVII', key)) \
                .replace('VII#', scale_degree_to_chord_root('VII#', key)) \
                .replace('VII', scale_degree_to_chord_root('VII', key)) \
                .replace('bVI', scale_degree_to_chord_root('bVI', key)) \
                .replace('VI#', scale_degree_to_chord_root('VI#', key)) \
                .replace('VI', scale_degree_to_chord_root('VI', key)) \
                .replace('bIV', scale_degree_to_chord_root('bIV', key)) \
                .replace('IV#', scale_degree_to_chord_root('IV#', key)) \
                .replace('IV', scale_degree_to_chord_root('IV', key)) \
                .replace('bV', scale_degree_to_chord_root('bV', key)) \
                .replace('V#', scale_degree_to_chord_root('V#', key)) \
                .replace('V', scale_degree_to_chord_root('V', key)) \
                .replace('bIII', scale_degree_to_chord_root('bIII', key)) \
                .replace('III#', scale_degree_to_chord_root('III#', key)) \
                .replace('III', scale_degree_to_chord_root('III', key)) \
                .replace('bII', scale_degree_to_chord_root('bII', key)) \
                .replace('II#', scale_degree_to_chord_root('II#', key)) \
                .replace('II', scale_degree_to_chord_root('II', key)) \
                .replace('bI', scale_degree_to_chord_root('bI', key)) \
                .replace('I#', scale_degree_to_chord_root('I#', key)) \
                .replace('I', scale_degree_to_chord_root('I', key))
