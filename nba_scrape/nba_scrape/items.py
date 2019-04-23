# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaScrapeItem(scrapy.Item):
    """
    Scraped Item from the basketballreference.com website table.

    Attributes
    ----------
    date : Field
        The date the game was played

    team_names : Field
        The first team name of the game.

    opponent_names : Field
        The second team name of the game.

    quarters : Field
        The quarter of the game.

    points : Field
        The points made by the first team within the quarter.  Not the opposing
        team.

    opponent_points : Field
        The points made by the opposing team within the quarter.

    diff_points : Field
        The difference in points between the team and the opposing team.  If
        negative then that means the team scored less than the opposing team.

    final_score : Field
        The final score between both teams throughout the game.  Not just the
        quarters.

    """

    date = scrapy.Field()
    team_names = scrapy.Field()
    opponent_names = scrapy.Field()
    quarters = scrapy.Field()
    points = scrapy.Field()
    opponent_points = scrapy.Field()
    diff_points = scrapy.Field()
    final_score = scrapy.Field()
