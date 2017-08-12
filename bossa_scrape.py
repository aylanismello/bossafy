import scrapy
import re

ARTIST_NAME = 'pixinguinha'

class BossaScrapeSpider(scrapy.Spider):
  name = 'bossa_scrape_spider'
  start_urls = ['https://www.cifraclub.com.br/' + ARTIST_NAME]

  def parse(self, response):
      title = response.css('.g-side-ad h1::text').extract_first()
      if title:
        #   we know the artist already
        #   artist = response.css('.g-side-ad h2::text').extract_first()
          url = response.url
          key = response.xpath('//span[@id="cifra_tom"]/a/text()').extract_first()
          chords = response.xpath('//pre//b/text()').extract()
          yield { 'title': title, 'artist': ARTIST_NAME, 'key': key, 'chords': chords, 'url': url }
      else:
          hrefs = response.css('.art_musics a::attr("href")').extract()
          urls = set([href for href in hrefs if (re.match( r'/' + ARTIST_NAME + '/([a-z0-9\-]+)/$', href ))])
          for url in urls:
              yield response.follow(url, self.parse)

    #   we have entered the
