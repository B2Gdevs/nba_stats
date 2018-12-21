# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.loader import ItemLoader
from nba_scrape.items import NbaScrapeItem


class BasketballReferenceSpider(CrawlSpider):
    name = 'basketball_reference'
    allowed_domains = ['www.basketball-reference.com']
    start_urls = ['https://www.basketball-reference.com/play-index/tscore.cgi?request=1&match=single&year_'\
                  'min=2013&year_max=2019&quarter_is_1=Y&quarter_is_2=Y&quarter_is_3=Y&quarter_is_4=Y&quarter_is_'\
                  '5=Y&is_playoffs=N&order_by=date_game&order_by_asc=Y']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[text()='Next page']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        # date_game_rows = response.xpath("//td[@data-stat='date_game']/a/text()").extract()
        # team_name_rows = response.xpath("//td[@data-stat='team_name']/a/text()").extract()
        # opponent_rows = response.xpath("//td[@data-stat='opp_name']/a/text()").extract()
        # quarter_rows = response.xpath("//td[@data-stat='quarter']/text()").extract()
        # point_rows = response.xpath("//td[@data-stat='pts']/text()").extract()
        # opp_pts_rows = response.xpath("//td[@data-stat='opp_pts']/text()").extract()
        # pts_diff_rows = response.xpath("//td[@data-stat='pts_diff']/text()").extract()
        # final_score_rows = response.xpath("//td[@data-stat='score_final']/text()").extract()
        loader = ItemLoader(item=NbaScrapeItem(), response=response)
        loader.add_xpath("date", "//td[@data-stat='date_game']/a/text()")
        loader.add_xpath("team_names", "//td[@data-stat='team_name']/a/text()")
        loader.add_xpath("opponent_names", "//td[@data-stat='opp_name']/a/text()")
        loader.add_xpath("quarters", "//td[@data-stat='quarter']/text()")
        loader.add_xpath("points", "//td[@data-stat='pts']/text()")
        loader.add_xpath("opponent_points", "//td[@data-stat='opp_pts']/text()")
        loader.add_xpath("diff_points", "//td[@data-stat='pts_diff']/text()")
        loader.add_xpath("final_score", "//td[@data-stat='score_final']/text()")

        yield loader.load_item()


        # for index, date in enumerate(date_game_rows):
        #     print("{}, {}, {}, {}, {},  {}, {},  {}".format(\
        #     date_game_rows[index], team_name_rows[index], opponent_rows[index], quarter_rows[index],\
        #     point_rows[index], opp_pts_rows[index], pts_diff_rows[index], final_score_rows[index]))


        # yield{
        #     "date_games" :date_game_rows,
        #     "team_names" :team_name_rows,
        #     "opponent_names" : opponent_rows,
        #     "quarters" : quarter_rows,
        #     "points" : point_rows,
        #     "opponent_points" : opponent_rows,
        #     "diff_points" : pts_diff_rows,
        #     "final_score" : final_score_rows

        # }
        