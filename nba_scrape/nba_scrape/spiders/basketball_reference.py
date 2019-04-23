# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from nba_scrape.items import NbaScrapeItem


class BasketballReferenceSpider(CrawlSpider):
    """
    Spider that scrapes basketballreference.com.

    This Spider is specifically looking for what teams have scored during a 
    quarter against another team.

    Attributes
    ----------
    Please refer to the scrapy documentation on the attributes used in this
    spider. https://docs.scrapy.org/en/latest/topics/spiders.html

    """

    name = 'basketball_reference'
    allowed_domains = ['www.basketball-reference.com']
    start_urls = ['https://www.basketball-reference.com/play-index/tscore.cgi'
                  '?request=1&match=single&year_min=2013&year_max=2019&quarter'
                  '_is_1=Y&quarter_is_2=Y&quarter_is_3=Y&quarter_is_4=Y&'
                  'quarter_is_5=Y&is_playoffs=N&order_by=date_game&'
                  'order_by_asc=Y']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[text()='Next page']"),
             callback='parse_item', follow=True))

    def parse_item(self, response):
        """
        Parse the item and push the data in to an NbaScrapeItem.

        This method gathers the data from the webpage and pushes it in to 
        a NbaScrapeItem since that will ensure that it gets picked up by a
        pipeline set up in the settings.py file.

        Parameters
        ----------
        response : response
            The response is the response object which is the response from
            the server when a spider begins crawling.

        Yields
        ------
        item : NbaScrapeItem
            This yields a loaded NbaScrapeItem

        """
        loader = ItemLoader(item=NbaScrapeItem(), response=response)
        loader.add_xpath("date", "//td[@data-stat='date_game']/a/text()")
        loader.add_xpath("team_names", "//td[@data-stat='team_name']/a/text()")
        loader.add_xpath("opponent_names", "//td[@data-stat='opp_name']/a/text"
                         + "()")
        loader.add_xpath("quarters", "//td[@data-stat='quarter']/text()")
        loader.add_xpath("points", "//td[@data-stat='pts']/text()")
        loader.add_xpath("opponent_points", "//td[@data-stat='opp_pts']/text()"
                         )
        loader.add_xpath("diff_points", "//td[@data-stat='pts_diff']/text()")
        loader.add_xpath("final_score", "//td[@data-stat='score_final']/text()"
                         )

        yield loader.load_item()
