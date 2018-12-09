
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:02:01 2017

@author: Talha.Iftikhar
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
import pandas as pd
from scrapy.http.request import Request


class QuotesSpider(CrawlSpider):
    name = "quotes"
    start_urls = [
        'http://www.colgate.com/en/us/oc/oral-health/find-a-dentist?IN_SPECIALTY=&IN_ZIP=&IN_LNAME='
    ]
   # rules = (Rule(LinkExtractor(),callback="parse_start_url", follow= True),)
    
    def parse_start_url(self,response):
        
       zips=pd.read_csv('ziplist/test1zip.csv')
       zipscolumn=zips["Zip Code"]
       for row in zipscolumn:
            print(row)
            link='http://www.colgate.com/en/us/oc/oral-health/find-a-dentist?IN_SPECIALTY=&IN_ZIP='+str(row)+'&IN_LNAME='
            req=Request(url=link,callback=self.parse_details)
            yield req 
 
    def parse_details(self, response):
        for row in  response.xpath('//div[@class="second-col"]'):
                item={}
                item["Dentist Name"]=row.xpath('div[1]/p/text()').extract_first()
                item["Address"]=row.xpath('div[1]/p[2]/a/text()').extract()
                specialty=str(row.xpath('div[2]/p[1]/text()').extract_first())
                #spstrip= specialty.strip().split(':')[1]
                item["Specialty"]=specialty.split(':')[-1]
                item["Phone"]=row.xpath('div[2]/p[2]/a/text()').extract_first()
                item["Map url"]=row.xpath('div[1]/p[2]/a/@href').extract_first()
              #  item["City"]=row.xpath('td/table/tbody/tr[1]/td[2]/p/small/span/text()').extract_first()
               # item["Date"]=row.xpath('td/table/tbody/tr[2]/td[1]/p/text()').extract_first()
                yield item
                #'author': quote.css('small.author::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            
############################################33
#    def parse(self, response):
 #       page = response.url.split("/")[-2]
  #      filename = 'quotes-%s.html' % page
   #     with open(filename, 'wb') as f:
    #        f.write(response.body)
     #   self.log('Saved file %s' % filename)
     
     #rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="link pageNextPrev {page:2}"]',)),\
     #             callback="parse_page", follow= True),)
#zip_codesfile=pd.read_csv('us_postal_codes.csv')
#zip_codesfile.info()
#zip_codes=zip_codesfile["Zip Code"]
#for row in zip_codes:
 #   print(row)
        
