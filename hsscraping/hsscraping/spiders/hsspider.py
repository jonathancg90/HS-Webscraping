# encoding=utf-8

import json
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hsscraping.items import HsscrapingItem

#Autor : Jonathan Carrasco Garcia

class HsSpider (BaseSpider):
    name = "helloworld"
    start_urls = [     
        'http://www.allhscodes.com/'
    ]

    def parse(self, response):
        parser = HtmlXPathSelector(response)
        tables = parser.select('//body/div[3]/table')
        return form_requests