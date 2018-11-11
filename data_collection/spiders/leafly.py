from data_collection.items import CannabisStrain
from pprint import pprint
from scrapy import Request, Spider
from scrapy.loader import ItemLoader


class ScrapeLeafly(Spider):
    """
    Pulls information for all the strains for which Leafly has information by reading from their A-Z index page.
    """
    name = "scrape-leafly"
    total_strains = 2591  # FIXME -- scrape this from the page instead
    strains_per_page = 48
    all_strains_url = "https://www.leafly.com/explore/page-{}/sort-alpha"

    def start_requests(self):
        num_pages = self.total_strains // self.strains_per_page
        for page_num in range(0, num_pages + 1):
            yield Request(url=self.all_strains_url.format(page_num), callback=self.parse)

    def parse(self, response):
        strain_detail_links = response.css(".ga_Explore_Strain_Tile").xpath('@href').extract()
        for strain_link in strain_detail_links:
            yield response.follow(strain_link, callback=self.parse_strain_detail)

    def parse_strain_detail(self, response):
        loader = ItemLoader(item=CannabisStrain(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('name', '//div[@class="copy--centered"]/h1/text()')
        loader.add_xpath('description', 'string(//div[@class="description"]/p)')
        loader.add_xpath('parent_strains', '//div[contains(@class, "strain__lineage")]//li/a/@href')
        # The Effects and Medical Uses are presented on the page as a histogram relative to each other
        histogram_xpath = '//div[@class="m-histogram" and @ng-show="currentAttributeTab===\'{}\'"]' \
                          '//div[contains(@class, "copy--sm")]/text()'
        loader.add_xpath('common_effects', histogram_xpath.format('Effects'))
        loader.add_xpath('medical_uses', histogram_xpath.format('Medical'))
        loader.add_xpath('negatives', histogram_xpath.format('Negatives'))
        loader.add_xpath('flavors', '//section[contains(@class, "strain__flavors")]//li/@title')
        pprint(loader.load_item())
