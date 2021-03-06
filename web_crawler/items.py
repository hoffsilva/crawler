# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobTitle = scrapy.Field()
    companyName = scrapy.Field()
    jobDescription = scrapy.Field()
    companyURL = scrapy.Field()
    applyURL = scrapy.Field()
    tags = scrapy.Field()
    pass
