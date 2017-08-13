import random, sys, json, constants
from IPython import embed
from collections import defaultdict

class MarkovChain(object):
    def __init__(self):
        self.open_corpus()
        self.distribution = self.generate_n_gram_distribution()

    def generate_n_gram_distribution(self, n=2):
        distribution = defaultdict(list)
        # this acts as our terminal character as well
        prev_chord = '.'

        for chord in self.CORPUS:
            distribution[prev_chord].append(chord)
            prev_chord = chord

        return distribution

    def next_chord(self, chord):
        if chord in self.distribution.keys():
            return random.choice(self.distribution.get(chord))
        else:
            return '.'

    def open_corpus(self):
        with open(constants.CHORD_CORPUS_PATH) as chords:
            self.CORPUS = chords.read().split(' ')
