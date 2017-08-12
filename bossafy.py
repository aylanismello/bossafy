import subprocess, json
import os
from selenium import webdriver
from collections import defaultdict
from IPython import embed

class Bossafy(object):
    ARTISTS_FILE_PATH = './data/config.json'
    CHORDS_FILE_PATH = './data/metadata/chord_dict.json'
    SCRAPED_SONGS_DIR_PATH = './data/song_scrapes/'

    def __init__(self, **kwargs):
        if kwargs.get('prep'):
            if kwargs.get('scrape'):
                self.scrape_songs()
            if kwargs.get('define_chords'):
                # maybe move this into its own module
                self.scrape_chord_definitions()

        # begin prompt
        print 'Done Bossafy-ing!'

    def open_or_create_chord_dict(self):
        try:
            with open(self.CHORDS_FILE_PATH, 'r') as data_file:
                chord_dict = json.load(data_file)
        except:
            print 'could not open %s, making new file' % (self.CHORDS_FILE_PATH)
            chord_dict = {}
        return chord_dict


    def scrape_chord_definitions(self):
        self.chord_dict = self.open_or_create_chord_dict()
        self.driver = webdriver.PhantomJS()
        urls_dict = {}

        for filename in os.listdir(self.SCRAPED_SONGS_DIR_PATH):
            with open("%s%s" % (self.SCRAPED_SONGS_DIR_PATH, filename), 'r') as scraped_song_file:
                urls_dict[filename.split('.')[0]] = [song['url'] for song in json.load(scraped_song_file)]

        # create/add to chord_dict
        for _, urls in urls_dict.iteritems():
            for url in urls:
                self.add_song_chords_to_dict(url)
            break

        # write chord_dict to .json
        with open(self.CHORDS_FILE_PATH, 'w') as data_file:
            json.dump(self.chord_dict, data_file, sort_keys=True, indent=2)

    def scrape_songs(self):
        with open(self.ARTISTS_FILE_PATH) as data_file:
            self.all_artists = json.load(data_file)['artists']

        for genre in self.all_artists.keys():
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
            print '%s already scraped!' % (NEW_FILE_NAME)

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
        print 'added chord-tab definitions from ' + url

# Bossafy(scrape=False, define_chords=False)
Bossafy()
