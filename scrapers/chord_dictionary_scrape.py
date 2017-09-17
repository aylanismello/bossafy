import json
from selenium import webdriver
from collections import defaultdict

driver = webdriver.PhantomJS()
CHORDS_FILE_NAME = './data/chord_dict.json'
SCRAPED_SONGS = './data/chico.json'



def add_song_chords_to_dict(chords, chord_tab_dict):
        # chord_tab_dict = {}
    for chord in chords:
        try:
            chord_name = chord.find_element_by_css_selector('strong').text
            chord_tab = chord.get_attribute('data-mount')
        except:
            # print 'could not get chord name or data-mount (chord tab)!'
            continue

        if not chord_tab or not chord_name:
            # print 'wtf... chord tab or chord nameis nothing! next!'
            continue

        chord_tab_dict[chord_name] = chord_tab
    return chord_tab_dict



def chords_in_tab_form():
    try:
        with open(SCRAPED_SONGS, 'r') as file_data:
            urls = []
            scraped_songs = json.load(file_data)

            for song in scraped_songs:
                urls.append(song['url'])
    except:
        print('CANNOT OPEN' + SCRAPED_SONGS)

    try:
        with open(CHORDS_FILE_NAME, 'r') as file_data:
            chord_tab_dict = json.load(file_data)
    except:
        print('could not open' + CHORDS_FILE_NAME + ', making new file')
        chord_tab_dict = {}

    for url in urls:
        driver.get(url)
        chords = driver.find_elements_by_css_selector('.chord')
        chord_tab_dict = add_song_chords_to_dict(chords, chord_tab_dict)
        print('added songs from ' + url)

    with open(CHORDS_FILE_NAME, 'w') as file_data:
        json.dump(chord_tab_dict, file_data, sort_keys=True, indent=2)





chords_in_tab_form()
