# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibosearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    post_url = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    content = scrapy.Field()
    comment_count = scrapy.Field()
    forward_count = scrapy.Field()
    praise_count = scrapy.Field()
    publish_time = scrapy.Field()
    create_time = scrapy.Field()
