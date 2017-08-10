import scrapy

class BossaScrapeSpider(scrapy.Spider):
  name = 'bossa_scrape_spider'
  start_urls = ['https://www.cifraclub.com.br/tom-jobim/wave/',
   'https://www.cifraclub.com.br/tom-jobim/o-morro-nao-tem-vez/']
  
  def parse(self, response):
    title = response.css('.g-side-ad h1::text').extract_first()
    yield { 'title': title }
    artist = response.css('.g-side-ad h2::text').extract_first()
    yield { 'artist': artist }
    key = response.xpath('//span[@id="cifra_tom"]/a/text()').extract_first()
    yield { 'key': key }
    chords = response.xpath('//pre//b/text()').extract()
    

    for chord in chords:
      yield {
        'chord': chord
      }

