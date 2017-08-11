# for chords in non_empty_chords:
#     for chord in chords:
#         if chord in chord_count.keys():
#             chord_count[chord] += 1
#         else:
#             chord_count[chord] = 1
#
#
# # sorted_chord_count = list(reverse(sorted(chord_count.items(), key=operator.itemgetter(1))))
# sorted_chord_count = sorted(chord_count.items(), key=operator.itemgetter(1))[::-1]
# print(sorted_chord_count)
