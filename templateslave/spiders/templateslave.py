from scrapy_redis.spiders import RedisSpider
from redis import Redis
import scrapy
from templateslave.items import TemplateslaveItem
from template.items import TemplateItem
import re

class templateslaveSpider(RedisSpider):
    name = 'templateslave'
    redis_key = "template:com_url"
    #"http://www.opensecrets.org/lobby/issuesum.php?id=TAX&year=2015"

    #获取所有公司链接
    def parse(self, response):
        item = TemplateslaveItem()
        item['com_name']=response.xpath('//*[@id="profileEntity"]/h1/text()').extract_first()
        item['com_url']=response.url
        item['year']=response.xpath('''
        //*[@id="profileLeftColumn"]/p[2]/strong/text()''').extract_first("").replace("Client Profile: Summary, ","")
        item["info"]=response.xpath('//*[@id="profileLeftColumn"]/p[4]/text()').extract_first("").strip()
        yield item