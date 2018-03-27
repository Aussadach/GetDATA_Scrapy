# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/currencies/bitcoin/']

    def parse(self, response):
        Number = response.xpath('//*[@class="text-large2"]/span/text()').extract()
        
        yield {'CURRENT BTC ':Number }
