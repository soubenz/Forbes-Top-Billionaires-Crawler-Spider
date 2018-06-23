# -*- coding: utf-8 -*-
 
import scrapy


class ForbesItem(scrapy.Item):
 
    name = scrapy.Field()
    age = scrapy.Field()
    wealthSource =  scrapy.Field()
    industry =  scrapy.Field()
    country =  scrapy.Field()
    gender =  scrapy.Field()
    lastName = scrapy.Field()
    worthChange =  scrapy.Field()
    position =  scrapy.Field()
    worth =  scrapy.Field()
    realTimePosition = scrapy.Field()
    realTimeWealth = scrapy.Field()
    image = scrapy.Field()
 
