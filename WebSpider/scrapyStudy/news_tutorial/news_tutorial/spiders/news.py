# -*- coding: utf-8 -*-
import scrapy

from news_tutorial.items import NewsTutorialItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.chinanews.com/scroll-news/news1.html']
    urls = []
    for i in range(1,10):
        urls.append('https://www.chinanews.com/scroll-news/news%d.html'%i)
    start_urls = urls

    def parse(self, response):
        news_info_list = response.css(".content_list>ul>li")
        item = NewsTutorialItem()
        for news_info in news_info_list:
            news_type = news_info.css(".dd_lm>a::text").extract_first()
            news_title = news_info.css(".dd_bt>a::text").extract_first()
            news_url = news_info.css(".dd_bt>a::attr(href)").extract_first()
            news_url = 'https:%s'%news_url
            item['news_type'] = news_type
            item['news_title'] = news_title
            item['news_url'] = news_url
            yield scrapy.Request(news_url,callback=self.detail_parse,meta={'item': item})

    def detail_parse(self, response):
        item = response.meta['item']
        news_article = response.css(".left_zw>p::text").extract()
        item['news_article'] = news_article
        yield item