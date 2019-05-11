# -*- coding: utf-8 -*-
import scrapy, re, time
from scrapy import FormRequest
from weibosearch.items import WeibosearchItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    # start_urls = ['http://weibo.cn/']

    search_url = 'https://weibo.cn/search/mblog'
    max_page = 200

    def start_requests(self):
        keyword = '000001'

        # 构造form data
        url = f"{self.search_url}?keyword={keyword}"

        for page in range(self.max_page + 1):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):
        weibos = response.xpath('//div[@class="c" and contains(@id,"M_")]')
        for weibo in weibos:
            # 如果是原创，那么他的span的class中有一个是cmt
            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').get())
            if is_forward:
                detail_url = weibo.xpath('.//a[contains(.,"原文评论[")]//@href').get()
            else:
                detail_url = weibo.xpath('.//a[contains(.,"评论[")]//@href').get()
            yield response.follow(detail_url, self.parse_detail)

    def parse_detail(self, response):
        id = re.search('comment\/(.*?)\?', response.url).group(1)
        post_url = response.url
        author = response.xpath('//*[@id="M_"]/div/a[1]/text()').get(default=None)
        author_url = response.xpath('//*[@id="M_"]/div/a[1]/@href').get(default=None)
        content = ''.join(response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract())
        comment_count = response.xpath('span[@class="pms"]//text()').re_first('评论\[(.*?)\]')
        forward_count = response.xpath('//a[contains(.,"转发[")]//text()').re_first('转发\[(.*?)\]')
        praise_count = response.xpath('//a[contains(.,"赞[")]//text()').re_first('赞\[(.*?)\]')
        publish_time = response.xpath('//div[@id="M_"]//span[@class="ct"]//text()').get(default=None)

        create_time = time.strftime("%Y-%m-%d %H:%M:%S")

        weibo_item = WeibosearchItem()
        for field in weibo_item.fields:
            weibo_item[field] = eval(field)
        yield weibo_item
