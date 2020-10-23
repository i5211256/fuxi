# -*- coding: utf-8 -*-
import scrapy


class App1Spider(scrapy.Spider):
    name = 'app1'
    # allowed_domains = ['hee']
    # start_urls = ['https://ip.cn']#需要换代理的网站
    def start_requests(self):
        for i in range(1,1000):
            start_urls = 'https://ip.cn'
            yield scrapy.Request(start_urls,self.show_ip,dont_filter=True)#将自动去重禁用
    def show_ip(selfs,response):
        ip = response.xpath('//*[@id="result"]/div/p[1]/code/text()').extract()
        print(ip)
