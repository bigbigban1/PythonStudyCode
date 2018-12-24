# -*- coding: utf-8 -*-
import time

import scrapy

from job_tutorial.items import JobItem


class JobSpider(scrapy.Spider):
    name = 'job'
    start_urls = ['http://search.51job.com/list/000000%252C00,000000,0000,00,9,99,python,2,1.html',]

    def parse(self, response):
        url_lists =  response.xpath('// *[ @ id = "resultList"] / div / p').css("::attr(href)").extract()
        #获取每个职位的详细url
        for url in url_lists:
            yield scrapy.Request(url,callback=self.detail_parse)
        next_url =  response.css("#resultList > div.dw_page > div > div > div > ul > li:nth-child(8) > a::attr(href)").extract_first()
        if next_url:
            yield scrapy.Request(next_url,callback=self.parse)


    def detail_parse(self,response):
        item = JobItem()
        try:
            #获取职位名
            job_name =  response.xpath("//div[@class='cn'] / h1").css("::text").extract_first()
            #获取公司名
            com_name = response.xpath("//div[@class='cn'] / p[@class='cname']").css("::text").extract()[1]
            #获取工作地点
            area = response.xpath("//div[@class='cn'] / p[@class='msg ltype']").css("::text").extract_first()
            #获取工作经验要求
            year = response.xpath("//div[@class='cn'] / p[@class='msg ltype']").css("::text").extract()[2]
            #获取学位要求
            degree = response.xpath("//div[@class='cn'] / p[@class='msg ltype']").css("::text").extract()[4]
            #获取招聘数量
            num = response.xpath("//div[@class='cn'] / p[@class='msg ltype']").css("::text").extract()[6]
            #获取发布日期
            date = response.xpath("//div[@class='cn'] / p[@class='msg ltype']").css("::text").extract()[8]
            #获取职位信息
            job_info = response.xpath("//div[@class='bmsg job_msg inbox']").css("::text").extract()
            #获取地点
            address = response.xpath("//div[@class='bmsg inbox']/p[@class='fp']").css("::text").extract()[2]
            #获取公司信息
            com_info = response.xpath("//div[@class='tmsg inbox']").css("::text").extract()
            item['job_name'] = job_name
            item['com_name'] = com_name
            item['area'] = area
            item['year'] = year
            item['degree'] = degree
            item['num'] = num
            item['date'] = date
            item['job_info'] = job_info
            item['address'] = address
            item['com_info'] = com_info
            yield item
        except BaseException:
            print("error")