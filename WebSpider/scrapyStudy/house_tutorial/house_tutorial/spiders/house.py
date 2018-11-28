# -*- coding: utf-8 -*-
import scrapy
from house_tutorial.items import HouseItem


class HouseSpider(scrapy.Spider):
    name = 'house'
    # allowed_domains = ['https://wh.zu.ke.com/zufang/rt200600000002/']
    url_list = []
    for i in range(1,100):
        url_list.append('https://wh.zu.ke.com/zufang/pg%drt200600000002/#contentList'%i)
    start_urls = url_list

    def parse(self, response):
        house_url_list = response.css(".content__list--item--aside::attr(href)").extract()
        for house_url in house_url_list:
            url = "https://wh.zu.ke.com%s"%house_url
            yield scrapy.Request(url,callback=self.detail_parse)

    def detail_parse(self, response):
        item = HouseItem()
        house_name = response.css(".content__title::text").extract_first()
        house_prise = response.css(".content__aside--title > span::text").extract_first()
        house_info = response.css(".content__article__info>ul>li::text").extract()
        house_intro = response.css("#desc > ul > li > p.threeline::text").extract_first()
        item["house_name"] = house_name
        item["house_prise"] = house_prise
        item["house_info"] = house_info
        item["house_intro"] = house_intro
        yield item

