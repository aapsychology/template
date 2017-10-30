import sys
import os
from scrapy.cmdline import execute
from redis import Redis

r=Redis()
for i in range(2001,2010):
    r.lpush('template:start_url','http://www.opensecrets.org/lobby/issuesum.php?id=TAX&year='+str(i))

sys.path.append(r'D:\project\template\template\spiders')
execute(['scrapy','crawl','template','-o','2001-2003.csv'])