import scrapy

# same as 
# class BrickSetSpid < scrapy.Spider
# note that we pick out the module in question from scrapy
# could have done: from scrapy import Spider
class BrickSetSpider(scrapy.Spider):
  name = "brickset_spider"
  start_urls = ['http://brickset.com/sets/year-2016']
  
  def parse(self, response):
    SET_SELECTOR = '.set'

    for brickset in response.css(SET_SELECTOR):
      NAME_SELECTOR = 'h1 a ::text'
      yield {
        'name': brickset.css(NAME_SELECTOR).extract_first(),
      }
