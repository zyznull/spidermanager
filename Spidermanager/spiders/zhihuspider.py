#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from Spidermanager.items import ArticleItem
import scrapy
import json
from io import *
import re
#import sys

#sys.stdout = TextIOWrapper(sys.stdout.buffer,encoding='UTF-8') #改变标准输出的默认编码  

class zhihuSpider(scrapy.Spider):
    name = "zhihu"
    author = ""
    start_urls = []
    def __init__(self,author,links,*args,**kwargs):
        super(zhihuSpider,self).__init__(*args,**kwargs)
        self.author = author
        self.start_urls.append(links)

    def start_requests(self):
        linkname = self.start_urls[0].split('/')[3]
        url = 'https://zhuanlan.zhihu.com/api/columns/'+linkname
        yield scrapy.Request(url,callback = self.get_num)


    def get_num(self,response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        num = jsonbody['postsCount']
        if num % 20 == 0:
            num = num // 20
        else:
            num = num // 20 + 1
        linkname = self.start_urls[0].split('/')[3]
        urls = 'https://zhuanlan.zhihu.com/api/columns/'+linkname+'/posts?limit=20&offset='
        for i in range(num):
            url = urls + str(i * 20)
            yield scrapy.Request(url,callback = self.parse)

    def parse(self, response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        pattern = re.compile(r'<[^>]+>', re.S)
        for ele in jsonbody:
            item = ArticleItem()
            item['link'] = 'https://zhuanlan.zhihu.com'+ ele['url']
            item['title'] = ele['title']
            item['author'] = self.author
            content = ele['content']
            item['desc'] = pattern.sub('', content)[:100]
            yield item
