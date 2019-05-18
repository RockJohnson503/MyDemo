# -*- coding: utf-8 -*-
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TimeoutError, TCPTimedOutError


class ErrbackExampleSpider(scrapy.Spider):
    name = 'errback_example'
    start_urls = [
        'http://www.httpbin.org/',
        'http://www.httpbin.org/status/404',
        'http://www.httpbin.org/status/500',
        'http://www.httpbin.org:12345/',
        'http://www.httphttpbinbin.org/',
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.errback_httpbin, dont_filter=True)

    def parse(self, response):
        self.logger.info('Got response from %s', response.url)

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)