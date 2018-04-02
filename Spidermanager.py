from scrapy import cmdline
from search import *

class SpiderManager(object):
    searchlist = {
        'weixin':weixin,
        'zhihu':zhihu,
        'douban':douban,
        'rss':rss,
        'weibo':weibo
    }
    
    def search(self,type,name):
        return self.searchlist[type].search(name)

    def crawl(sefl,type,url,author):
        cmdline.execute(('scrapy crawl '+type+' -a author='+author+' -a links='+url).split())

sp = SpiderManager()
link = sp.search(type = 'weibo',name = '不二大叔说')
print(link)
sp.crawl(type = 'weibo',url = link,author='不二大叔说')
