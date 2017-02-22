# -*- coding: utf-8 -*-
import scrapy
import xlwt
from costco.items import CostcoItem
from scrapy.selector import Selector

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from selenium import webdriver

chromedriver = "/Users/wangdong/Downloads/chromedriver"

class CostcoVitminsSpider(CrawlSpider):
    name = "costcovitmins"
    allowed_domains = ["costco.com"]
    start_urls = [
        'https://www.costco.com/CatalogSearch?pageSize=96&currentPage=1&keyword=All+Vitamins+%26+Supplements',
		]
        
    rules = (
        # try to match '/2015/09/04/regex/'
        Rule(LinkExtractor(allow=('product\..*\.html',)), callback="parse_item"),
        #Rule(LinkExtractor(allow=('html',)), callback="parse_item"),
        
        #Rule(LinkExtractor(allow=('2015/09/04/regex/', )), callback="parse_item"),
        #Rule(LinkExtractor(allow=(r'/\d{4}/\d{2}/\d{2}/.*', )), callback="parse_item"),
    )
    
    def __init__(self):
        super(CostcoVitminsSpider, self).__init__()
        self.driver = webdriver.Chrome(chromedriver)    
        
    def parse(self, response):
        
        #for link in LinkExtractor(allow=('product\..*\.html',)).extract_links(response):
            #print "this is link:"+str(link)
        
        return CrawlSpider.parse(self, response)
        
    def parse_item(self, response):
        self.logger.info('Hi, parse_item! %s', response.url)
        
        #self.driver = webdriver.Chrome(chromedriver)  
        
        #item = someItem()
        #item['url'] = link.url
        
        
        
        self.driver.get(response.url)
        item = CostcoItem()
        item['name'] = self.driver.find_element_by_xpath('//title').get_attribute('text')
    
        sPriceElement = self.driver.find_element_by_xpath('//div[@class="your-price row no-gutter"]')
        
        sPrice = sPriceElement.find_element_by_xpath('./span[@class="value"]').text
        
        sPrice=sPrice.replace(",", "")
        dPrice = float(sPrice)
        item['price'] = dPrice
        item['priceTax'] = dPrice * (1 + 0.085)
        item['priceCustom'] = dPrice * (1 + 0.085) + 15
        item['priceChinese'] = (dPrice * (1 + 0.085) + 15) * 6.75

        image_urls = self.driver.find_element_by_xpath('//img[@itemprop="image"]').get_attribute("src")

        item['image_urls'] = image_urls
        item['image_paths'] = image_urls
        
        print item['image_urls']
        print item['image_paths']
                 
        yield item
        pass
        
    