# -*- coding: utf-8 -*-

# Scrapy settings for weibosearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from weibosearch.middlewares import UaMiddleWare

BOT_NAME = 'weibosearch'

SPIDER_MODULES = ['weibosearch.spiders']
NEWSPIDER_MODULE = 'weibosearch.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'weibosearch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibosearch.middlewares.WeibosearchSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'weibosearch.middlewares.WeibosearchDownloaderMiddleware': 543,
# }
DOWNLOADER_MIDDLEWARES = {
    'weibosearch.middlewares.CookieMiddleWare': 543,
    'weibosearch.middlewares.UaMiddleWare': 544,
    # 'weibosearch.middlewares.ProxyMiddleWare': 545,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'weibosearch.pipelines.WeibosearchPipeline': 300,
    'weibosearch.pipelines.MongoPipeline': 301,
    # 'scrapy_redis.pipelines.RedisPipeline': 555

}

MONGO_URI = 'mongodb://192.168.20.253:27017/'
MONGO_DB = 'weibo'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_HOST = '192.168.20.253'
REDIS_PORT = 6379


COOKIES_POOL_URL = 'http://192.168.20.253:5000/weibo/random'

PROXY_POOL_URL = "http://192.168.20.253:5010/get/"

# 默认暂停scrapy,之后重启，不会爬取以前爬过的
# 设置下面这个为True,会在每次重启时候清空以前的信息，从零爬取
# SCHEDULER_FLUSH_ON_START = True

# # 爬完之后不清空redis中的request和指纹
# SCHEDULER_PERSIST = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

