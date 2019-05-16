# -*- coding: utf-8 -*-
import scrapy


class KuwoSpider(scrapy.Spider):
    name = 'kuwo'
    allowed_domains = ['kuwo.cn']
    start_urls = ['http://ts.kuwo.cn/service/gethome.php?act=new_home']

    def parse(self, response):
        print(response)
