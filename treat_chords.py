from mingus.core import progressions

def chord_root_to_scale_degree(root, key):
    return progressions.determine([root], key, True)[0]

def chord_to_relative(chord, key):
    return chord.replace('A', chord_root_to_scale_degree('A', key)) \
                .replace('A#', chord_root_to_scale_degree('A#', key)) \
                .replace('Ab', chord_root_to_scale_degree('Ab', key)) \
                .replace('B', chord_root_to_scale_degree('B', key)) \
                .replace('B#', chord_root_to_scale_degree('B#', key)) \
                .replace('Bb', chord_root_to_scale_degree('Bb', key)) \
                .replace('C', chord_root_to_scale_degree('C', key)) \
                .replace('C#', chord_root_to_scale_degree('C#', key)) \
                .replace('Cb', chord_root_to_scale_degree('Cb', key)) \
                .replace('D', chord_root_to_scale_degree('D', key)) \
                .replace('D#', chord_root_to_scale_degree('D#', key)) \
                .replace('Db', chord_root_to_scale_degree('Db', key)) \
                .replace('E', chord_root_to_scale_degree('E', key)) \
                .replace('E#', chord_root_to_scale_degree('E#', key)) \
                .replace('Eb', chord_root_to_scale_degree('Eb', key)) \
                .replace('F', chord_root_to_scale_degree('F', key)) \
                .replace('F#', chord_root_to_scale_degree('F#', key)) \
                .replace('Fb', chord_root_to_scale_degree('Fb', key)) \
                .replace('G', chord_root_to_scale_degree('G', key)) \
                .replace('G#', chord_root_to_scale_degree('G#', key)) \
                .replace('Gb', chord_root_to_scale_degree('Gb', key))
