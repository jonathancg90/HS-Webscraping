# -*- coding: utf-8 -*-

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
    	parser = HtmlXPathSelector(response.replace(body=response.body_as_unicode())) 
        #parser = HtmlXPathSelector(response)
        tables = parser.select('//body/div[3]/table')
        for table in tables:
        	filas = table.select('.//tr[position()>1]')
        	for fila in filas:
        		hs = HsscrapingItem()
        		code = fila.select('.//td[1]/text()').extract()
        		if '520812' in code:
        			import pdb;pdb.set_trace()
        		name = fila.select('.//td[2]/text()').extract()
        		yield HsscrapingItem(code=code, name=name)
        		#return hs