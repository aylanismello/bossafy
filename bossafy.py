import subprocess
import json
import os.path
from IPython import embed

class Bossafy(object):
    ARTISTS_FILE_NAME = './data/config.json'

    def __init__(self):
        with open(self.ARTISTS_FILE_NAME) as data_file:
            for genre in json.load(data_file)['artists'].keys():
                self.scrape_all_artists(genre)

    def scrape_all_artists(self, genre):
        for artist in self.get_artists(genre):
            formatted_artist = '-'.join(artist.lower().split(' '))
            url = "https://www.cifraclub.com.br/%s" % (formatted_artist)
            self.scrape_chords(formatted_artist, url)

    def get_artists(self, genre):
        with open(self.ARTISTS_FILE_NAME) as data_file:
            try:
                artists = json.load(data_file)['artists'][genre]
            except:
                print 'could not open %s' % (genre)
        return artists

    def scrape_chords(self, artist, url):
        # check if this file exists first
        NEW_FILE_NAME = "./data/song_scrapes/%s-scrape.json" % (artist)
        if not os.path.isfile(NEW_FILE_NAME):
            command = "scrapy runspider ./bossafy_scraper.py -a url=%s -a artist_name=%s -o %s" % (url, artist, NEW_FILE_NAME)
            subprocess.check_output(command, shell=True)
        else:
            print '%s already scraped!' % (NEW_FILE_NAME)


Bossafy()
