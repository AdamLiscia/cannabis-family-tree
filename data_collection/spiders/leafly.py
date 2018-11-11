from pprint import pprint
import scrapy


class ScrapeLeafly(scrapy.Spider):
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
            yield scrapy.Request(url=self.all_strains_url.format(page_num), callback=self.parse)

    def parse(self, response):
        strain_detail_links = response.css(".ga_Explore_Strain_Tile").xpath('@href').extract()
        for strain_link in strain_detail_links:
            yield response.follow(strain_link, callback=self.parse_strain_detail)

    def parse_strain_detail(self, response):
        pass
