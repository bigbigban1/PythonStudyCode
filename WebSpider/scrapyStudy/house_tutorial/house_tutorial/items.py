# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_name = scrapy.Field()
    house_prise = scrapy.Field()
    house_info = scrapy.Field()
    house_intro = scrapy.Field()