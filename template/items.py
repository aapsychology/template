# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TemplateItem(scrapy.Item):
    com_url=scrapy.Field()
    year=scrapy.Field()
    page=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
