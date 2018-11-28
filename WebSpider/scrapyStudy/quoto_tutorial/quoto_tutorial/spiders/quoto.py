# -*- coding: utf-8 -*-
import scrapy
from quoto_tutorial.items import QuotoItem


class QuotoSpider(scrapy.Spider):
    name = 'quoto'
    # allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        quotos = response.css('.quote')
        for quoto in quotos:
            item = QuotoItem()
            text = quoto.css('.text::text').extract_first()
            author = quoto.css('.author::text').extract_first()
            tags = quoto.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = 'http://quotes.toscrape.com%s'%next
        if url:
            yield scrapy.Request(url = url,callback = self.parse)