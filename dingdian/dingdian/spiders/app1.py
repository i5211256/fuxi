# -*- coding: utf-8 -*-
import scrapy
from dingdian.items import DingdianItem

class App1Spider(scrapy.Spider):
    name = 'app1'
    # allowed_domains = ['hee']
    start_urls = ['http://www.meishij.net/yaoshanshiliao/jibingtiaoli/weiyan/']

    def parse(self, response):


        for ms in response.xpath("//div[contains(@class,'i_w')]"):
            item = DingdianItem()
            title = ms.xpath("div/div/strong/text()").extract_first()
            hot = ms.xpath("div/div/span/text()").extract_first()
            item["title"] = title
            item["hot"] = hot
            yield item

        next_page = response.xpath("//a[@class='next']/@href").extract_first()
        print("下一页：", next_page)
        if next_page: yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
