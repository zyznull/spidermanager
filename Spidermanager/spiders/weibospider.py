#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from Spidermanager.items import ArticleItem
import scrapy
import json
from io import *
import re
import datetime
#import sys

#sys.stdout = TextIOWrapper(sys.stdout.buffer,encoding='UTF-8') #改变标准输出的默认编码  

class weiboSpider(scrapy.Spider):
    name = "weibo"
    author = ""
    start_urls = []
    def __init__(self,author,links,*args,**kwargs):
        super(weiboSpider,self).__init__(*args,**kwargs)
        self.author = int(author)
        self.start_urls.append(links)

    def start_requests(self):
        linkname = self.start_urls[0].split('/')[4]
        urls = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+linkname+'&containerid=107603'+linkname+'&page='
        for i in range(5):
            url = urls + str(i)
            yield scrapy.Request(url,callback = self.parse)


    def parse(self, response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        pattern = re.compile(r'<[^>]+>', re.S)
        for ele in jsonbody['data']['cards']:
            item = ArticleItem()
            item['url'] = ele['scheme']
            item['topic_id'] = self.author
            item['title'] = ''
            text = ele['mblog']['text']
            text = pattern.sub('', text)
            length = min(100,len(text))
            item['abstract'] = text[:length]
            item['publish_time'] = datetime.datetime.now()
            yield item
