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
urlname = sp.search(type = 'zhihu',name = u'金与火之歌')
print(urlname)
sp.crawl(type = 'zhihu',author = u'1',url = urlname)

