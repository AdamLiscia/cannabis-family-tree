# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CannabisStrain(scrapy.Item):
    """
    Contains information about a particular strain of cannabis scraped from its detail page.
    """
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    parent_strains = scrapy.Field()
    common_effects = scrapy.Field()
    medical_uses = scrapy.Field()
    negatives = scrapy.Field()
    flavors = scrapy.Field()
