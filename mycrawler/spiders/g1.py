import scrapy
from mycrawler.items import MycrawlerItem
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor

class G1Spider(CrawlSpider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ["https://g1.globo.com",]

    def parse(self, response):

        if response.url == "https://g1.globo.com":
            #import ipdb; ipdb.set_trace()
            le = LinkExtractor(
                    deny=('/globonews/playlist/',),
                    restrict_xpaths=('//div[@class="feed-post-body"]//a'),
                )

            base = le.extract_links(response)

            for i, item in enumerate(base):
                if i == 0:
                    yield scrapy.Request(url=item.url, callback=self.parse_manchete)
                else:
                    yield scrapy.Request(url=item.url, callback=self.parse_news)

        else:
            pass

    def parse_news(self, response):
        i = MycrawlerItem()

        # import ipdb; ipdb.set_trace()

        i['title'] = response.xpath('//h1[@class="content-head__title"]//text()').extract_first()
        i['subTitle'] = response.xpath('//h2[@class="content-head__subtitle"]//text()').extract_first()  
        i['author'] =  response.xpath('//p[@class="content-publication-data__from"]/text()').extract_first()  
        i['fullText'] = response.xpath('//article//p').extract()
        i['img'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        i['headLine'] =  False
        i['newsPaper'] = 5
        i['section'] = 1
        i['link'] = response.url

        #import ipdb; ipdb.set_trace()
        
        return i

    def parse_manchete(self, response):
        i = MycrawlerItem()

        #import ipdb; ipdb.set_trace()

        i['title'] = response.xpath('//h1[@class="content-head__title"]//text()').extract_first()
        i['subTitle'] = response.xpath('//h2[@class="content-head__subtitle"]//text()').extract_first()  
        i['author'] =  response.xpath('//p[@class="content-publication-data__from"]/text()').extract_first()  
        i['fullText'] = response.xpath('//article//p').extract()
        i['img'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        i['headLine'] =  True
        i['newsPaper'] = 5
        i['section'] = 1
        i['link'] = response.url

        #import ipdb; ipdb.set_trace()

        return i

    def parse_colunista(self, response):
        pass
