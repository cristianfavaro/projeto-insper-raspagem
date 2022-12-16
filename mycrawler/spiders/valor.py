import scrapy
from mycrawler.items import MycrawlerItem
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor

class ValorSpider(CrawlSpider):
    name = 'valor'
    allowed_domains = ['valor.globo.com']
    start_urls = ["https://valor.globo.com/", "https://valor.globo.com/opiniao/maria-cristina-fernandes/",]

    def parse(self, response):
        if response.url == "https://valor.globo.com/":

            
            le = LinkExtractor(
                    deny=('.com/eu-e/', '.com/carreira/', '.com/opiniao/', '.com/eu-e/'),
                    restrict_xpaths=('//div[contains(@class, "highlight__title") or contains(@class, "highlight__links")]//a'),
                )
            base = le.extract_links(response)

            for i, item in enumerate(base):
                if i == 0:
                    yield scrapy.Request(url=item.url, callback=self.parse_manchete)
                else:
                    yield scrapy.Request(url=item.url, callback=self.parse_news)

        else:

            le = LinkExtractor(
                    restrict_xpaths=('//div[contains(@class, "feed-post-body-title")]//a'),
                )
            base = le.extract_links(response)

            for item in base:
                yield scrapy.Request(url=item.url, callback=self.parse_colunista)


    def parse_news(self, response):
        i = MycrawlerItem()
        # import ipdb; ipdb.set_trace()

        i['title']  = response.xpath('//h1//text()').extract_first()
        i['subTitle'] = response.xpath('//h2//text()').extract_first()
        i['author'] = response.xpath('//p[@class="content-publication-data__from"]/text()').extract_first()  
        i['fullText'] = response.xpath('//article//p').extract()
        i['img'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        i['headLine'] = False
        i['newsPaper'] = 4
        i['section'] = 1
        i['link'] = response.url

        #import ipdb; ipdb.set_trace()

        return i

    def parse_manchete(self, response):
        
        i = MycrawlerItem()

        i['title']  = response.xpath('//h1//text()').extract_first()
        i['subTitle'] = response.xpath('//h2//text()').extract_first()
        i['author'] = response.xpath('//p[@class="content-publication-data__from"]/text()').extract_first()  
        i['fullText'] = response.xpath('//article//p').extract()
        i['img'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        i['headLine'] = True
        i['newsPaper'] = 4
        i['section'] = 1
        i['link'] = response.url

        #import ipdb; ipdb.set_trace()

        return i

    def parse_colunista(self, response):

        i = MycrawlerItem()
        
        i['title']  = response.xpath('//h1//text()').extract_first()
        i['fullText'] = response.xpath('//article//p').extract()
        i['img'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        i['headLine'] =  False
        i['newsPaper'] = 4
        i['section'] = 1
        i['link'] = response.url

        #import ipdb; ipdb.set_trace()
        #continue atalho legal

        return i
