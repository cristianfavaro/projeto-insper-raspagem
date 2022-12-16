from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from mycrawler.spiders.g1 import G1Spider
from mycrawler.spiders.valor import ValorSpider

process = CrawlerProcess(get_project_settings())
process.crawl(G1Spider)
process.crawl(ValorSpider)
process.start()
