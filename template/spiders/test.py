from scrapy_redis.spiders import RedisSpider
from redis import Redis
import scrapy
from template.items import TemplateItem
import re

ptt=re.compile(r'.*page=(\d+)')
page=ptt.match('issuesum.php?id=TAX&year=2016&sort=a&page=2')
print(page.groups()[0])

r=Redis()
list=['http://www.opensecrets.org/lobby/clientsum.php?id=D000000262&year=2002',
      'http://www.opensecrets.org/lobby/clientsum.php?id=D000000262&year=2003',
      'http://www.opensecrets.org/lobby/clientsum.php?id=D000000262&year=2004',
      'http://www.opensecrets.org/lobby/clientsum.php?id=D000000262&year=2002']

for aa in list:
    bb=r.sadd('testfull',aa)
    if bb==0:
        pass
    else:
        r.lpush('template:com_url',aa)
        print(aa)
        print(type(aa))
        print ('good')