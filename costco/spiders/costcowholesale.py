# -*- coding: utf-8 -*-
import scrapy
import xlwt
from costco.items import CostcoItem
from scrapy.selector import Selector

from selenium import webdriver

chromedriver = "/Users/wangdong/Downloads/chromedriver"

class CostcowholesaleSpider(scrapy.Spider):
    name = "costcowholesale"
    allowed_domains = ["costco.com"]
    start_urls = [
        # 'http://www.costco.com/',
		'http://www.costco.com/Nature-Made-CoQ10-200-mg.%2c-140-Softgels.product.100118306.html',
		'http://www.costco.com/Schiff%C2%AE-Move-Free%C2%AE-Advanced%2c-170-Tablets.product.100048006.html',
        'http://www.costco.com/Nature-Made%C2%AE-Fish-Oil-1200-mg%2c-400-Softgels.product.11751262.html',
        'http://www.costco.com/Nature\'s-Bounty%C2%AE-Fish-Oil-1%2c400-mg.%2c-130-Softgels.product.100006067.html',
        'http://www.costco.com/Similac%C2%AE-Advance%C2%AE-Non-GMO*-Infant-Formula-2-pack%3b-34-oz.-Each.product.100231391.html',
        'http://www.costco.com/HP-63XL-Ink-Cartridge-Combo-Pack-.product.100232842.html',
        #'http://www.costco.com/.product.11751262.html',
        'https://www.costco.com/Alienware-15-Laptop---Intel-Core-i7---6GB-NVIDIA-Graphics---1080p.product.100315342.html',
        'https://www.costco.com/ASUS-ROG-GL752VW-Laptop---Intel-Core-i7---1080p---4GB-NVIDIA-Graphics.product.100315459.html',
        'https://www.costco.com/ASUS-ROG-GL552VW-Laptop---Intel-Core-i7---4GB-NVIDIA-Graphics---4K-Ultra-HD.product.100307811.html',
		]
    
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver)
    
    #===========================================================================
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse,
    #         endpoint='render.html',
    #         args={'wait': 0.5},
    #         )
    #===========================================================================

    def parse(self, response):

        self.driver.get(response.url)

        print "Here it is:"        
        print str(response)
        #print response.body_as_unicode
        
        #sel = Selector(response)
        item = CostcoItem()
        #item['name'] = self.driver.find_element_by_xpath('//title/text()').extract()
        item['name'] = self.driver.find_element_by_xpath('//title').get_attribute('text')
        
        
        print 'itemname:'+item['name']
        
        #=======================================================================
        # for element in self.driver.find_elements_by_tag_name('title'):
        #     print "text:"+element.get_attribute('text')
        #     print "tag_name:"+element.tag_name
        #     print "parent:"+element.parent
        #     print "location:"+element.location
        #     print "size:"+element.size
        #=======================================================================
        
        #print "goog:"+item['name']
        
        #print sel.xpath('//div[re:test(@class, "your-price")]').extract()
        #print self.driver.find_element_by_xpath('//div[@id="product-details"]').extract()
        
        #sPrice = response.xpath('//div[(@class="your-price")]/span[re:test(@class, "value")]/text()').extract()
        #sPrice = self.driver.find_element_by_xpath('//div[re:test(@class, "your-price")]/span[(@class="value")]/text()').extract()
        #sPrice2 = self.driver.find_element_by_xpath('//div[re:test(@class, "marketing-container")]/span[(@class="unitcurrency")]/text()').extract()


        #=======================================================================
        # sPrice = self.driver.find_element_by_xpath('//div[@class="your-price"]/span[@class="value"]').get_attribute('text')
        # #sPrice = self.driver.find_element_by_xpath(
        # sPrice2 = self.driver.find_element_by_xpath('//div[@class="marketing-container"]/span[@class="unitcurrency"]').get_attribute('text')
        #=======================================================================

        sPriceElement = self.driver.find_element_by_xpath('//div[@class="your-price row no-gutter"]')
        
        sPrice = sPriceElement.find_element_by_xpath('./span[@class="value"]').text
        
        
        print "sPrice:"+sPrice
        #sPrice = self.driver.find_element_by_xpath(
        #sPrice2Element = self.driver.find_element_by_xpath('//div[@class="marketing-container form-group"]')

        #sPrice2 = sPrice2Element.find_element_by_xpath('./span[@class="unitcurrency"]').text
        
        
        #print "sPrice:"+sPrice

        #print sPrice2
        print 'listtests'
        print sPrice
        #sPrice = sPrice[0][0:].strip()
        #dPrice = float(sPrice)
        sPrice=sPrice.replace(",", "")
        dPrice = float(sPrice)
        item['price'] = dPrice
        item['priceTax'] = dPrice * (1 + 0.085)
        item['priceCustom'] = dPrice * (1 + 0.085) + 15
        item['priceChinese'] = (dPrice * (1 + 0.085) + 15) * 6.75

        #image_urls = response.xpath('//img[@itemprop="image"]/@src').extract()
        image_urls = self.driver.find_element_by_xpath('//img[@itemprop="image"]').get_attribute("src")
        #image_urls = image_urls_elem.find_element_by_xpath('.//img[@itemprop="image"]')

        item['image_urls'] = image_urls
        #item['image_paths'] = image_urls[0][image_urls[0].rfind('/') + 1:]
        item['image_paths'] = image_urls
        
        print item['image_urls']
        print item['image_paths']
                 
        yield item
        pass

#    def start_requests(self):
# 		yield Request("http://www.costco.com",headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
# 			"})
		# pass

