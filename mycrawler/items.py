# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MycrawlerItem(scrapy.Item):
    title = scrapy.Field()
    subTitle = scrapy.Field()
    author = scrapy.Field()
    fullText = scrapy.Field()
    img = scrapy.Field()
    headLine = scrapy.Field()
    newsPaper = scrapy.Field()
    section = scrapy.Field()
    link = scrapy.Field()