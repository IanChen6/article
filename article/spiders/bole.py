# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class BoleSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1.获取文章列表页所有文章的url，并交给scrapy下载后解析
        2.获取下一页的url，交给scrapy进行下载，下载后交给1
        :param response:
        :return:
        '''

       #解析列表页的所有文章的url，并交给scrapy进行下载
        post_urls=response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            # response.url+post_url 如果当前post url不完整，要拼接（response.url为当前域名）
            yield Request(url=post_url,callback=self.parse_detail)
            # yield Request(url=parse.urljoin(response.url+post_url),callback=self.parse_detail)
            # print(post_url)
        #提取下一页并进行下载
        next_url=response.css("#archive > div.navigation.margin-20 > a.next.page-numbers::attr(href)").extract_first("")
        if next_url:
        # yield Request(url=parse.urljoin(response.url + post_url), callback=self.parse)#列表页，继续执行parse
            yield Request(url=next_url, callback=self.parse)
    def parse_detail(self,response):
        #css选择器
        title=response.css('#widgets-homepage-fullwidth > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(1)::text')
        title.extract()
        pass
