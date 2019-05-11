# encoding: utf-8

"""
File: quotes_spider.py
Author: Rock Johnson
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls= [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page:
            yield response.follow(next_page, self.parse)