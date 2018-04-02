import scrapy
import json
import re
import random
from Spidermanager.items import ArticleItem

class weixinSpider(scrapy.Spider):
    name = "weixin"
    start_urls = ['https://mp.weixin.qq.com']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    }
    query = ''
    def __init__(self,author,links,*args,**kwargs):
        super(weixinSpider,self).__init__(*args,**kwargs)
        self.author = author
        self.query = links

    def start_requests(self):
        with open('cookie.txt', 'r', encoding='utf-8') as f:
            cookie = f.read()
        cookies = json.loads(cookie)
        yield scrapy.Request(self.start_urls[0],callback = self.parse1,headers = self.header,cookies = cookies,meta = {'cookies':cookies})

    def urlencode(self,parameters):
        st = ''
        for (key,value) in parameters.items():
            st = st + key + '=' + str(value) + '&'
        st = st[:-1]
        return st
    def parse1(self,response):
        token = re.findall(r'token=(\d+)', str(response.url))[0]
        response.meta['token'] = token
        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        query_id = {
        'action': 'search_biz',
        'token' : token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': self.query,
        'begin': '0',
        'count': '5'
        }
        yield scrapy.Request(search_url + self.urlencode(query_id),callback = self.parse2,headers = self.header,cookies = response.meta['cookies'],meta = response.meta)

    def parse2(self,response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        lists = jsonbody.get('list')[0]
        fakeid = lists.get('fakeid')
        response.meta['fakeid'] = fakeid
        appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        query_id_data = {
        'token': response.meta['token'],
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',#不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
        }
        yield scrapy.Request(appmsg_url + self.urlencode(query_id_data),callback = self.parse3,headers = self.header,cookies = response.meta['cookies'],meta = response.meta)

    def parse3(self,response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        print(jsonbody)
        max_num = jsonbody.get('app_msg_cnt')
        num = int(int(max_num) / 5)
        appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        begin = 0
        while num > 0:
            query_id_data = {
            'token': response.meta['token'],
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(str(begin)),
            'count': '5',
            'query': '',
            'fakeid': response.meta['fakeid'],
            'type': '9'
            }
            num -= 1
            begin = int(begin)
            begin+=5
            yield scrapy.Request(appmsg_url + self.urlencode(query_id_data),callback = self.parse,headers = self.header,cookies = response.meta['cookies'],meta = response.meta)

    def parse(self,response):
        jsonbody = json.loads(response.body.decode('utf-8','ignore'))
        fakeid_list = jsonbody.get('app_msg_list')
        for fake in fakeid_list:
            item = ArticleItem()
            item['title'] = fake['title']
            item['link'] = fake['link']
            item['author'] = self.query
            item['desc'] = ''
            yield item