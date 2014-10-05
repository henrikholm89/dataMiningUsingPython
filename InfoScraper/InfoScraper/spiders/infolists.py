# -*- coding: utf-8 -*-

import scrapy
from InfoScraper.items import InfoListItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


INFO_LIST_PAGES = ['weekend', 'kultur', 'indland', 'udland', 'debat', 'protokol']

class InformationSpider(CrawlSpider):
    name = 'infolist'
    allowed_domains = ['information.dk']
    start_urls = ["http://www.information.dk/indland"] #['http://www.information.dk/%s' % page for page in INFO_LIST_PAGES] #
    rules = ( Rule (SgmlLinkExtractor(restrict_xpaths=('//li[@class="pager-next"]/a',))
                    , follow= True),
              Rule(SgmlLinkExtractor(restrict_xpaths=('//h3[@class="node-title"]')), callback='parse_item')
        )


    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = InfoListItem()
        item['title'] = []
        item['infoid'] = []
        for sel in response.xpath('//h3[@class="node-title"]/a/text()').extract():
          item['title'].append(sel)
        #item['title'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        for sel in response.xpath('//h3[@class="node-title"]/a/@href').extract():
          item['infoid'].append(sel)
        for i in item:
          self.log('[%s] %s' % (i['infoid'], i['title']))
          print i['infoid'], i['title']
        return item
