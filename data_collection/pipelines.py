# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from data_collection.spiders.leafly import ScrapeLeafly


class StrainParentsPipeline(object):
    """
    Processes the CannabisStrain items coming out of the spiders. Cleans the fields that are length-one lists and
    converts relative URLs to absolute ones.
    """
    def process_item(self, item, spider):
        if spider.__class__ == ScrapeLeafly:
            item["name"] = item["name"][0]
            item["url"] = item["url"][0]
            item["description"] = item["description"][0]
            item["parent_strains"] = [f'https://www.leafly.com{strain_url}' for strain_url in item["parent_strains"]]
        return item
