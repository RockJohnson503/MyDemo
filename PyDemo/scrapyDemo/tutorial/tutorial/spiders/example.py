# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/page/1/',
        'http://quotes.toscrape.com/tag/humor/page/2/',
        'http://quotes.toscrape.com/tag/humor/page/3/',
    ]

    def parse(self, response):
        for h3 in response.css("h3").getall():
            yield {'title': h3}

        for href in response.css('a').getall():
            yield response.follow(href, self.parse)