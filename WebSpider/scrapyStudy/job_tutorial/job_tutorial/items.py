# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    com_name = scrapy.Field()
    area = scrapy.Field()
    year = scrapy.Field()
    degree = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()
    job_info = scrapy.Field()
    address = scrapy.Field()
    com_info = scrapy.Field()

