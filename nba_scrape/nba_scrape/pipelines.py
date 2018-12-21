# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class NbaScrapePipeline(object):
    def __init__(self):
        pass
    
    def open_spider(self, spider):
        self.df = pd.DataFrame()
        

    def close_spider(self, spider):
        self.df.to_csv("data.csv")

    def process_item(self, item, spider):
        if self.df.empty:
            self.df = pd.DataFrame.from_dict(dict(item))
            
        else:
            df_ = pd.DataFrame.from_dict(dict(item))
            self.df = pd.concat([self.df, df_])
        
        # return item
