import sys, os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(__file__))
execute(['scrapy', 'crawl', 'weibo'])
