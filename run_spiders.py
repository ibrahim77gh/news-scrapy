# run_spiders.py
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news.spiders.seattle_spider import *
from news.spiders.hedge_spider import *
from news.spiders.rockwell_spider import *

def run_spiders():
    process = CrawlerProcess(get_project_settings())
    process.crawl(PoliticsSpider)
    process.crawl(SportsSpider)
    process.crawl(BusinessSpider)
    process.crawl(LocalnewsSpider)
    process.crawl(HedgeSpider)
    process.crawl(RockwellSpider)
    # Add other spider names here
    process.start()

