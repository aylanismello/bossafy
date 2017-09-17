import subprocess, json
import constants
from markov_chain import MarkovChain
import os
from selenium import webdriver
from collections import defaultdict
from IPython import embed
# from treat_chords import chord_to_relative, relative_to_chord

class Bossafy(object):

    def __init__(self, **kwargs):
        if kwargs.get('prep'):
            if kwargs.get('scrape'):
                self.scrape_songs()
            if kwargs.get('define_chords'):
                # maybe move this into its own module
                self.scrape_chord_definitions()

        # corpus seems to recreated everytime here
        # self.update_chord_corpus()
        self.markov_chain = MarkovChain()

        self.chord_dict = self.open_or_create_chord_dict()

        # the user input function will become the logic in an endpoint
        # while True:
        #     self.get_user_input()

        # begin prompt
        print('Done Bossafy-ing!')

    def get_user_input(self, chord, chord_type):
        # chord = raw_input('Is chord in TAB form or CHORD form?  0 to exit.\n')
        #
        # if chord == '0':
        #     exit()

        if chord_type.lower() == 'chord':
            tab = self.chord_dict.get(chord)
            # self.loop_over_new_chords(chord_or_tab)
            return self.get_next_chord(chord)

        # elif chord_type.lower() == 'tab':
        #     chord_or_tab = raw_input('Input tab. Must be in form 3x333x \n')
        #     # if it's in the same form as stored in dictionary, that's cool too
        #     if len(chord_or_tab) == 11:
        #         formatted_tab = chord_or_tab
        #     else:
        #         tab_chars = [c for c in chord_or_tab[:6]]
        #         formatted_tab = ' '.join(tab_chars).upper()
        #
        #     try:
        #         chord = self.chord_dict.keys()[self.chord_dict.values().index(formatted_tab)]
        #     except ValueError as err:
        #         print 'tab form of chord not found in chord dictionary!'


    # def loop_over_new_chords(self, chord):
    #     # last_chord = self.print_next_chord(chord)
    #     #
    #     # try_again = True
    #     #
    #     # while try_again:
    #     #     wants_another_chord = raw_input('want another chord? y/n/NEW \n or to get a new chord from this one? ')
    #     #     if wants_another_chord.lower() == 'new':
    #     #         last_chord = self.print_next_chord(last_chord)
    #     #     else:
    #     #         try_again = True if (wants_another_chord.lower() != 'n') else False
    #     #         if try_again:
    #     #             self.print_next_chord(chord)

    def get_next_chord(self, chord):
        new_chord = self.markov_chain.next_chord(chord)
        new_tab = self.chord_dict.get(new_chord)
        # print 'try %s ( %s ) as a next chord for %s' % (new_chord, new_tab, chord)
        return { 'name': new_chord, 'tab': new_tab }

    # def update_chord_corpus(self):
    #     for filename in os.listdir(constants.SCRAPED_SONGS_DIR_PATH):
    #         with open("%s%s" % (constants.SCRAPED_SONGS_DIR_PATH, filename), 'r') as scraped_song_file:
    #             scraped_data = json.load(scraped_song_file)
    #             print('opened %s' % (filename))
    #
    #         with open(constants.CHORD_CORPUS_PATH, 'w') as corpus_file:
    #             print('going to write chord corpus!')
    #             for song in [song for song in scraped_data if song['chords'] and song['key']]:
    #                 for chord in song['chords']:
    #                     # refactor this BS plz
    #                     chord = chord.replace('\xb0', 'dim')
    #                     chord = chord.replace('\xba', 'dim')
    #                     chord = chord.replace('\xe9', 'dim')
    #                     chord = chord.replace('\xea', 'dim')
    #                     chord = chord.replace('\xf3', 'dim')
    #                     chord = chord.replace('\xe3', 'dim')
    #                     chord = chord.replace('\xe1', 'dim')
    #                     chord = chord.replace('\xe7', 'dim')
    #                     chord = chord.replace('\u2019', 'dim')
    #                     chord = chord.replace('\u2028', 'dim')
    #                     # relative_chord = chord_to_relative(chord, song['key'])
    #                     # corpus_file.write('%s ' % (relative_chord))
    #
    #                     corpus_file.write('%s ' % (chord))
    #                     # check for weird cases here
    #                 # put end of song delimter mark of . here
    #                 corpus_file.write('. ')

    def open_or_create_chord_dict(self):
        try:
            with open(constants.CHORDS_FILE_PATH, 'r') as data_file:
                chord_dict = json.load(data_file)
        except:
            print('could not open %s, making new file' % (constants.CHORDS_FILE_PATH))
            chord_dict = {}
        return chord_dict

    def scrape_chord_definitions(self):
        self.chord_dict = self.open_or_create_chord_dict()
        self.driver = webdriver.PhantomJS()
        urls_dict = {}

        for filename in os.listdir(constants.SCRAPED_SONGS_DIR_PATH):
            if 'chico' in filename or 'tom' in filename:
                continue
            with open("%s%s" % (constants.SCRAPED_SONGS_DIR_PATH, filename), 'r') as scraped_song_file:
                urls_dict[filename.split('.')[0]] = [song['url'] for song in json.load(scraped_song_file)]

        # create/add to chord_dict
        for _, urls in urls_dict.items():
            for url in urls:
                self.add_song_chords_to_dict(url)
            break

        # write chord_dict to .json
        with open(constants.CHORDS_FILE_PATH, 'w') as data_file:
            json.dump(self.chord_dict, data_file, sort_keys=True, indent=2)

    def scrape_songs(self):
        with open(constants.ARTISTS_FILE_PATH) as data_file:
            self.all_artists = json.load(data_file)['artists']

        for genre in list(self.all_artists.keys()):
            self.scrape_all_artists(genre)

    def scrape_all_artists(self, genre):
        for artist in self.all_artists[genre]:
            formatted_artist = '-'.join(artist.lower().split(' '))
            url = "https://www.cifraclub.com.br/%s" % (formatted_artist)
            self.scrape_chords(formatted_artist, url)

    def scrape_chords(self, artist, url):
        NEW_FILE_NAME = "./data/song_scrapes/%s-scrape.json" % (artist)
        if not os.path.isfile(NEW_FILE_NAME):
            command = "scrapy runspider ./scrapes/bossafy_scraper.py -a url=%s -a artist_name=%s -o %s" % (url, artist, NEW_FILE_NAME)
            subprocess.check_output(command, shell=True)
        else:
            print('%s already scraped!' % (NEW_FILE_NAME))

    def add_song_chords_to_dict(self, url):
        self.driver.get(url)
        chords = self.driver.find_elements_by_css_selector('.chord')
        for chord in chords:
            try:
                chord_name = chord.find_element_by_css_selector('strong').text
                chord_tab = chord.get_attribute('data-mount')
            except:
                # could not get chord name or data-mount (chord tab)!
                continue

            if not chord_tab or not chord_name:
                # wtf... chord tab or chord nameis nothing! next!
                continue

            self.chord_dict[chord_name] = chord_tab
        print('added chord-tab definitions from ' + url)

# Bossafy(define_chords=True, prep=True)
# Bossafy()
