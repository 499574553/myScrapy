from scrapy.spiders.init import InitSpider
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class CoachSpider(scrapy.Spider):
    name = 'uscis'
    allowed_domains = ['uscis.gov']
    #login_page = 'https://qq.corporateperks.com/login/login'
    start_urls = ['https://egov.uscis.gov/casestatus/landing.do',
                   ]
    

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'appReceiptNum': 'EAC1790024073'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
#         if "Welcome, Wang" in response.body:
#              self.log("Successfully logged in. Let's start crawling!")
#         else:
#              self.log("Bad times :(")
#         
#         pass

        if "Enter Another Receipt Number" in response.body:
            str = response.xpath('//div[@class="rows text-center"]/h1/text()').extract()
            detail = response.xpath('//div[@class="rows text-center"]/p/text()').extract()
            self.log("success!")        
            print str[0]+'\n'+detail[0]
        else:
            self.log("The application receipt number entered is invalid.")




    #===========================================================================
    # rules = (
    #     Rule(LinkExtractor(allow=r'-\w+.html$'),
    #          callback='parse_item', follow=True),
    # )
    #===========================================================================

#===============================================================================
#     def init_request(self):
#         """This function is called before crawling starts."""
#         return Request(url=self.login_page, callback=self.login)
# 
#     def login(self, response):
#         """Generate a login request."""
#         
#         print "login?"
#         return FormRequest.from_response(response,
#                     formdata={'login': '499574553@qq.com', 'password': 'wzm19870125'},
#                     callback=self.check_login_response)
# 
#     def check_login_response(self, response):
#         """Check the response returned by a login request to see if we are
#         successfully logged in.
#         """
#         
#         if "Welcome, Wang" in response.body:
#             self.log("Successfully logged in. Let's start crawling!")
#             # Now the crawling can begin..
#             self.initialized()
#         else:
#             self.log("Bad times :(")
#             # Something went wrong, we couldn't log in, so nothing happens.
# 
#     #def parse_item(self, response):
#         #print 'passe_item'
#         
#     def parse(self, response):
#         print 'passe_item'
#===============================================================================
