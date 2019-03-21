# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
This script is used by the Scrapy project to scrape a website.
After scraping the website the project creates NbaScrapeItems which is used
by the pipeline in this script and converted in to a csv file for use in
the main application.

Author: Benjamin Garrard
"""
import pandas as pd


class NbaScrapePipeline():
    """
    Scrapy pipeline for NbaScrapeItems.

    This pipeline is used to take in the scrapy items from the items.py file
    and then format them in to a usable form for other applications.  This
    pipeline should be set in the settings.py file.

    """

    def __init__(self):
        """Do nothing."""
        pass

    def open_spider(self, spider):
        """
        Create DataFrame when the spider begins.

        Parameters
        ----------
        spider : spider
            The spider that uses this pipeline will automatically be passed
            to this method since this is a method that is looked for in a 
            pipeline.
        """
        self.df = pd.DataFrame()

    def close_spider(self, spider):
        """
        Save the data when the spider stops scraping.

        Parameters
        ----------
        spider : spider
            The spider that uses this pipeline will automatically be passed
            to this method since this is a method that is looked for in a 
            pipeline.

        """
        self.df.to_csv("data.csv")

    def process_item(self, item, spider):
        """
        Process the data and push it in to the dataframe.

        Parameters
        ----------
        item : NbaScrapeItem
            The item is an NbaScrapeItem that has the raw data pushed in to
            it during the scraping process in the BasketballReferenceSpider.

        spider : spider
            The spider that uses this pipeline will automatically be passed
            to this method since this is a method that is looked for in a
            pipeline.

        """
        if self.df.empty:
            self.df = pd.DataFrame.from_dict(dict(item))

        else:
            df_ = pd.DataFrame.from_dict(dict(item))
            self.df = pd.concat([self.df, df_])
