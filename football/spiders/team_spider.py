import scrapy

from football.items.items import FootballItem


class OddsSpider(scrapy.Spider):
    name = "odds"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://trade.500.com/jczq/"
    ]

    def parse(self, response):
        for sel in response.xpath('//tr[@class="bet-tb-tr"]'):
            item = FootballItem()
            item['home'] = sel.xpath('a/text()').extract()
            print(sel)
