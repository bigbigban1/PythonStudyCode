# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem

from job_tutorial.items import JobItem


class JobCleanPipeline(object):
    def process_item(self, item, spider):
        #清洗工作名
        # job_name_str = '|'.join(item['job_name'])
        item['job_name'] = item['job_name'].replace("\r\n", "").replace("\t", "")
        #清洗公司名
        # com_name_str = '|'.join(item['com_name'])
        item['com_name'] = item['com_name'].replace("\r\n", "").replace("\t", "")
        #清洗工作地点
        # area_str = '|'.join(item['area'])
        item['area'] = item['area'].replace("\r\n", "").replace("\t", "").replace("\xa0","")
        #清洗工作经验要求
        # year_str = '|'.join(item['year'])
        item['year'] = item['year'].replace("\xa0", "")
        #清洗学历要求:
        # degree_str = '|'.join(item['degree'])
        item['degree'] = item['degree'].replace("\xa0", "")
        #招聘数量
        # num_str = '|'.join(item['num'])
        item['num'] = item['num'].replace("\xa0", "")
        #发布日期
        # date_str = '|'.join(item['date'])
        item['date'] = item['date'].replace("\xa0", "").replace("\t", "")
        #职位信息
        # job_info_str = '|'.join(item['job_info'])
        item['job_info'] = ''.join(item['job_info']).replace("\r\n", "").replace("\t", "").replace("\xa0", "")
        #地点
        # address_str = '|'.join(item['address'])
        item['address'] = item['address'].replace("\t", "")
        #公司信息
        # com_info_str = '|'.join(item['com_info'])
        item['com_info'] = ''.join(item['com_info']).replace("\r\n", "").replace("\t", "").replace("\xa0","").replace("\xa0?","")
        return item

class MongoPipline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db['job'].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()