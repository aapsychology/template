# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TemplateslaveItem(scrapy.Item):
    com_name=scrapy.Field()
    com_url=scrapy.Field()
    info=scrapy.Field()
    year=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
