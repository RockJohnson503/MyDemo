# -*- coding: utf-8 -*-
import scrapy


class MysearchSpider(scrapy.Spider):
    name = 'mysearch'
    start_urls = ['https://www.zhipin.com/']

    def parse(self, response):
        print(self.settings.attributes.keys())
        # return scrapy.FormRequest.from_response(
        #     response,
        #     formdata={'account': '18223203525', 'password': 'k836867547'},
        #     callback=self.after_search
        # )

    def after_search(self, response):
        self.logger.info(response.text)