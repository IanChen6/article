# -*- coding: utf-8 -*-
import scrapy


class WenzhangSpider(scrapy.Spider):
    name = 'wenzhang'
    allowed_domains = ['news.baidu.com/']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):
        response.xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a')
        title=response.xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a/txt()').extract()[0]
        # content=response.xpath('//div[contains("@id=,"guojie")]')
        content=response.xpath('//*[@id="guojie"]')
        print(title)
        print(content)
        pass
