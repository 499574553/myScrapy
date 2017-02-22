# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CostcoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    priceTax = scrapy.Field()
    priceCustom = scrapy.Field()
    priceChinese = scrapy.Field()

    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    
    pass
