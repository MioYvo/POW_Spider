__author__ = 'mio'
#-*- coding: utf-8 -*-

#from scrapy.spider import BaseSpider
from scrapy.spider import Spider
from scrapy.selector import Selector
#from scrapy.selector import HtmlXPathSelector
from NuptTiebaSpider.items import NuptPOWItem
from NuptTiebaSpider.creat_table import CreatTable

class NuptPOWSpider_1(Spider):
    name = "POWS1"
    allowed_domains = ["teiba.baidu.com"]
    start_urls = [
        "http://tieba.baidu.com/f?kw=nupt&fr=index"
    ]

    def parse(self, response):
        #sel = HtmlXPathSelector(response)
        sel = Selector(response)
        topics = sel.xpath('//*[@class="j_thread_list clearfix"]')
        items = []
        ct = CreatTable()
        ct.creat()

        for topic in topics:
            item = NuptPOWItem()
            item['rep_num'] = topic.xpath('div/div[1]/div/text()').extract()
            item['title'] = topic.xpath('div/div[2]/div[1]/div[1]/a/@title').extract()
            item['title_url'] = topic.xpath('div/div[2]/div[1]/div[1]/a/@href').extract() #problem /p/xxxxxxxx  need tieba.baidu.com/p/xxxxxxx
            item['author'] = topic.xpath('div/div[2]/div[1]/div[2]/span/a/text()').extract()
            #item['author_homepage'] = topic.xpath('div/div[2]/div[1]/div[2]/span/a/@href').extract() #homepage url
            item['topic_desc'] = topic.xpath('div/div[2]/div[2]/div[1]/div[1]/div/text()').extract()
            item['topic_desc_img'] =topic.xpath('div/div[2]/div[2]/div[1]/div[2]/div/div/ul/li/div/img/@src').extract()
            item['last_rep_time'] = topic.xpath('div/div[2]/div[2]/div[2]/span[2]/text()').extract()
            item['last_rep_aur'] = topic.xpath('div/div[2]/div[2]/div[2]/span[1]/a/text()').extract() #last_rep_aur改	为author_homepage的抓取地址，懒得改那么多了
            #item['last_rep_aur'] = topic.xpath('div/div[2]/div[1]/div[2]/span/a/@href').extract()
            #item['last_rep_aur_home'] = topic.xpath('div/div[2]/div[2]/div[2]/span[1]/a/@href').extract()
            item['last_rep_aur_home'] = topic.xpath('div/div[2]/div[1]/div[2]/span/a/@href').extract()
            items.append(item)
        return items
