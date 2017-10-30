import scrapy
import requests
import time
from bs4 import BeautifulSoup
import sys
import os

class template(scrapy.Spider):
    name = 'template2'
    start_urls = ['http://www.opensecrets.org/lobby/issuesum.php?id=TAX&year=2011']

    def parse(self, response):
        year = response.xpath('//*[@id="profileLeftColumn"]/h1/text()').extract_first().replace('Issue Profile, ',"")
        for company in response.xpath('//*[@id="issue_summary"]/tbody/tr'):
            name= company.xpath('td[1]/a/text()').extract_first()
            link=company.xpath('td[1]/a/@href').extract_first()
            full_url='http://www.opensecrets.org/lobby/'+link
            res = requests.get(full_url)
            time.sleep(1)
            soup = BeautifulSoup(res.text, 'lxml')
            yield{'year':year,
                 'name':name,
                  'info':soup.find_all('p')[5].text.strip()}
        next_page=response.xpath('//div[@class="pageCtrl"]/a/@href').extract()[-1]
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)


