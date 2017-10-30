from scrapy_redis.spiders import RedisSpider
from redis import Redis
import scrapy
from template.items import TemplateItem
import re
import time
from template.utils.bloomfilter import PyBloomFilter,conn

class templateSpider(RedisSpider):
    name = 'template'
    redis_key = "template:start_url"
    #"http://www.opensecrets.org/lobby/issuesum.php?id=TAX&year=2015"

    #获取所有公司链接
    def parse(self, response):
        r = Redis()
        item = TemplateItem()
        com_urls= response.xpath('//*[@id="issue_summary"]/tbody/tr/td[1]/a/@href')

        for com_url in com_urls:
            com_url=com_url.extract()
            bf=PyBloomFilter(conn=conn,key='to_fil_url')
            bf.add(com_url)
            aa=bf.is_exist(com_url)
            time.sleep(0.3)
            if aa==0:
                pass
            else:
                full_url = 'http://www.opensecrets.org/lobby/' + com_url
                r.lpush('template:com_url',full_url)
                item["year"] = response.xpath('//*[@id="profileLeftColumn"]/h1/text()').extract_first().replace(
                    "Issue Profile, ", "")
                ptt=re.compile(r'.*page=(\d+)$')
                item["page"]=int((re.match(ptt,
                    response.xpath('//div[@class="pageCtrl"]/a/@href').extract()[-1])).groups()[0])-1
                item["com_url"] = full_url
                yield item
        next_page=response.xpath('//div[@class="pageCtrl"]/a/@href').extract()[-1]
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
