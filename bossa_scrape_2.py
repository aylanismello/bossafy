import scrapy
import re

class BossaScrapeSpider(scrapy.Spider):
  name = 'bossa_scrape_spider_2'
  start_urls = ['https://www.cifraclub.com.br/tom-jobim/']

  def parse(self, response):
      title = response.css('.g-side-ad h1::text').extract_first()
      if title:
        #   we know the artist
        #   artist = response.css('.g-side-ad h2::text').extract_first()
          key = response.xpath('//span[@id="cifra_tom"]/a/text()').extract_first()
          chords = response.xpath('//pre//b/text()').extract()
          yield { 'title': title, 'artist': 'Tom Jobim', 'key': key, 'chords': chords }
      else:
          hrefs = response.css('.art_musics a::attr("href")').extract()
          urls = set([href for href in hrefs if (re.match( r'/tom-jobim/([a-z0-9\-]+)/$', href ))])
          for url in urls:
              yield response.follow(url, self.parse)

    #   we have entered the
