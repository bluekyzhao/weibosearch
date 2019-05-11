# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from weibosearch.items import WeibosearchItem
import re, time
import pymongo


class WeibosearchPipeline(object):
    # 对ITEM中的字段进行统一化处理
    def parse_time(self, ttime):
        # 对新浪微博的复杂时间格式处理
        if re.match('\d+月\d+日', ttime):
            ttime = time.strftime('%Y-', time.localtime()) + ttime
            ttime = ttime.replace('月', '-').replace('日', ' ')
        if re.match('\d+分钟前', ttime):
            minute = re.match('(\d+)', ttime).group(1)
            ttime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(minute) * 60))
        if re.match('.*今天', ttime):
            ttime = re.match('今天(.*)', ttime).group(1).strip()
            ttime = time.strftime('%Y-%m-%d', time.localtime()) + ' ' + ttime
        return ttime

    def process_item(self, item, spider):
        if item.get('content'):
            item['content'] = item['content'].lstrip(':').strip()

        if item.get('publish_time'):
            item['publish_time'] = self.parse_time(item['publish_time'].strip())
        return item


class MongoPipeline:
    # 存储到MongoDB
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # 这个函数在spider启动时候，自动调用
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 先在数据库中查询，有的话就更新，没有的话就查询
        self.db.WeiboContent.update({'id': item['id']}, {'$set': dict(item)}, True)
        return item
