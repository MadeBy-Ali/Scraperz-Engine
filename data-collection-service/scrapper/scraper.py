from scrapy.crawler import CrawlerProcess
from .spiders.ecommerce_spider import ECommerceSpider

def run_scrapper():
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "ERROR",  # Quiet logs for simplicity
    })
    process.crawl(ECommerceSpider)
    process.start()
