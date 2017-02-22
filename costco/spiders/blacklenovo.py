# -*- coding: utf-8 -*-
import scrapy
import xlwt
from costco.items import CostcoItem
from scrapy.selector import Selector

import time 

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/wangdong/Downloads/chromedriver"


from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
firefoxdriver = FirefoxBinary('/Users/wangdong/Downloads/geckodriver')

class blacklenovoSpider(CrawlSpider):
    name = "blacklenovo"
    allowed_domains = ["zaq.us"]
    start_urls = [
        'https://zaq.us/lenovo/',
		]
        
    def __init__(self):
        super(blacklenovoSpider, self).__init__()
        #self.driver = webdriver.Firefox()
        self.driver=webdriver.Chrome(chromedriver)    
         
    def parse(self, response):
        
        #for link in LinkExtractor(allow=('product\..*\.html',)).extract_links(response):
            #print "this is link:"+str(link)
        self.driver.get(response.url)
        
        #str = response.xpath('//ins[@class="adsbygoogle"]').extract()
        #time.sleep(2)
        str = self.driver.find_element_by_xpath('//ins[@class="adsbygoogle"]')
        
        str.click()
        time.sleep(2)
        
        #self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
        #self.driver.execute_script('var win = window.open(“”,”_self”); win.close();')
            
        print "visiting.................."
        print str
        
        time.sleep(2)
        self.driver.quit()
        
        #with open("log2", "wb") as outfile:
            #outfile.write(time.strftime(format)+"\n")
        #yield scrapy.Request(url="https://zaq.us/lenovo/",
            #callback=self.parse,
            #dont_filter=True)

