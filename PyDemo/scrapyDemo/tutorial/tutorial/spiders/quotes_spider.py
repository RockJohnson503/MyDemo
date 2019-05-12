# encoding: utf-8

"""
File: quotes_spider.py
Author: Rock Johnson
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # for quote in response.css('.quote'):
        #     yield {
        #         'text': quote.css('.text::text').get(),
        #         'author': quote.css('.author::text').get(),
        #         'tags': quote.css('.tags .tag::text').getall(),
        #     }

        # for a in response.css('.author + a'): # This is author pages
        #     yield response.follow(a, callback=self.parse_author, priority=1)
        #
        # for a in response.css('.next a'): # This is next pages
        #     yield response.follow(a, callback=self.parse, priority=2)

        for quote in response.css('.quote'):
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
            }

        for a in response.css('.next a'): # This is next pages
            yield response.follow(a, callback=self.parse, priority=2)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('.author-title::text'),
            'birthday': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }