# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem


class NovelTutorialPipeline(object):
    def process_item(self, item, spider):
        if item['article']:
            # for index,value in enumerate(item['article']):
            #     item['article'][index] = item['article'][index].replace('\xa0','')
            #     item['article'][index] = item['article'][index].replace('<br>\r\n', '')
            s = '|'.join(item['article'])
            s1 = s.replace('\xa0','').replace('<br>\r\n', '').replace('<div id="content">','').replace('</div>','')
            item['article'] = s1.split('|')
            return item
        else:
            return DropItem('Missing article')

class MongoPipline(object):

    def __init__(self,mongo_uri,mongo_db):
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
        self.db['novel'].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()
