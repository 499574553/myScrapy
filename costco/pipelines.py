# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from scrapy.contrib.pipeline.images import ImagesPipeline
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import xlwt
import xlsxwriter
from xlsxwriter.workbook import Workbook

ezxf = xlwt.easyxf

class CostcoPipeline(object):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 0
    font0.bold = True
    style0 = xlwt.XFStyle()
    style0.font = font0
    style0.alignment.wrap = 1

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    workbook = xlsxwriter.Workbook('/Users/wangdong/Desktop/costco3.xls')
    worksheet = workbook.add_worksheet()

    format0 = workbook.add_format()
    format0.set_text_wrap()

    heading_xf = ezxf('font: bold on; align: wrap on, vert centre, horiz centre')

    heading = ['Name', 'Price', 'AddTax', 'CustomPrice', 'ChinaPrice']
    rows = 0
    for colx, value in enumerate(heading):
        ws.write(rows, colx, value, heading_xf)

    count = 1

    def process_item(self, item, spider):
        self.ws.write(self.count,0, item['name'], self.style0)
        self.ws.write(self.count,1, item['price'], self.style0)
        self.ws.write(self.count,2, item['priceTax'], self.style0)
        self.ws.write(self.count,3, item['priceCustom'], self.style0)
        self.ws.write(self.count,4, item['priceChinese'], self.style0)
        #self.ws.insert_image(self.count, 5, settings['IMAGES_STORE']+'/'+item['image_paths'],{'x_scale': 0.5, 'y_scale': 0.2,'positioning': 3})

        self.worksheet.write(self.count, 0, item['name'], self.format0)
        self.worksheet.write(self.count, 1, item['price'], self.format0)
        self.worksheet.write(self.count, 2, item['priceTax'], self.format0)
        self.worksheet.write(self.count, 3, item['priceCustom'], self.format0)
        self.worksheet.write(self.count, 4, item['priceChinese'], self.format0)
        self.worksheet.insert_image(self.count, 5, settings['IMAGES_STORE']+'/'+item['image_paths'],{'x_scale': 0.5, 'y_scale': 0.2,'positioning': 3})

        #settings = crawler.settings
        if settings['IMAGES_STORE']:
            print settings['IMAGES_STORE']
        #self.ws.insert_image(self.count,5, "")

        #self.ws.insert_image(self.count,5, settings['IMAGES_STORE']+'/'+item['image_paths'][0])
        #self.ws.insert_bitmap(settings['IMAGES_STORE']+'/'+item['image_paths'][0], self.count, 5)

        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        #print settings['IMAGES_STORE']+'/'+item['image_paths'][0]
        #print item['image_paths'][0]
         
        self.count = self.count+1
        self.wb.save('/Users/wangdong/Desktop/costco.xls')
	return item


    def close_spider(self, spider):
        self.workbook.close()
        #self.client.close()


class MyImagesPipeline(ImagesPipeline):
    
    image_name = 'hello'
    

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        
        #print "hellohellohello"+'full/%s' % (image_name)
        return 'full/%s' % (image_guid)

    def get_media_requests(self, item, info):
        #for image_url in item['image_urls']:
        #image_name = item['name']
        yield scrapy.Request(item['image_urls'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        #print "helloworld:"+image_paths
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths[0]
        #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        #print image_paths
        return item
 
