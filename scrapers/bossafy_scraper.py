import scrapy
import re


class BossafyScraper(scrapy.Spider):

  name = 'bossafy_scraper'

  def __init__(self, url, artist_name):
      self.url, self.artist_name = url, artist_name
      self.start_urls = [url]

  def parse(self, response):
      title = response.css('.g-side-ad h1::text').extract_first()
      if title:
          url = response.url
          key = response.xpath('//span[@id="cifra_tom"]/a/text()').extract_first()
          chords = response.xpath('//pre//b/text()').extract()
          yield { 'title': title, 'artist': self.artist_name, 'key': key, 'chords': chords, 'url': url }
      else:
          hrefs = response.css('.art_musics a::attr("href")').extract()
          urls = set([href for href in hrefs if (re.match( r'/' + self.artist_name + '/([a-z0-9\-]+)/$', href ))])
          for url in urls:
              yield response.follow(url, self.parse)
