# -*- coding: utf-8 -*-
import scrapy


class BtcShowSpider(scrapy.Spider):
    name = 'Btc_show'
    allowed_domains = ['coinmarketcap.com/currencies/bitcoin']
    start_urls = ['http://coinmarketcap.com/currencies/bitcoin/']

    def parse(self, response):
        Number = response.xpath('//*[@class="text-large2"]/text()').extract()
        Number.append(response.xpath('//*[@class="details-text-medium"]/text()').extract()[0])
        
        yield {'CURRENT BTC ':Number }
    