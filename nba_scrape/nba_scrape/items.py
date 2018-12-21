# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    team_names = scrapy.Field()
    opponent_names = scrapy.Field()
    quarters = scrapy.Field()
    points = scrapy.Field()
    opponent_points = scrapy.Field()
    diff_points = scrapy.Field()
    final_score = scrapy.Field()
    
