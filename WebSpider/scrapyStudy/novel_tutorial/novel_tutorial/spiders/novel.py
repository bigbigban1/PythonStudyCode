# -*- coding: utf-8 -*-
import scrapy
from novel_tutorial.items import NovelItem


class NovelSpider(scrapy.Spider):
    # custom_settings = {}
    name = 'novel'
    # allowed_domains = ['www.biquge.com.tw/18_18820/8643948.html']
    start_urls = ['http://www.biquge.com.tw/18_18820/8643948.html']

    def parse(self, response):
        item = NovelItem()
        title = response.css('.bookname > h1::text').extract_first()
        articles = response.css('#content').extract()
        # for article in articles:
        #     article.replace('<br>\r\n','')
        #     article.replace('\xa0', '')
        item['title'] = title
        item['article'] = articles
        yield item
        next = response.css('#wrapper > div.content_read > div > div.bottem2 > a:nth-child(4)::attr(href)').extract_first()
        if next:
            url = response.urljoin(next)
            yield scrapy.Request(url,callback=self.parse)