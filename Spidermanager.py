from scrapy import cmdline
from search import *
<<<<<<< HEAD
from threading import Thread
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor,defer
=======
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
>>>>>>> 6618d3153ebaf6a07500f6bf0cc5d3a6954bbf18

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
       # cmdline.execute(('scrapy crawl '+type+' -a author='+author+' -a links='+url).split())
       process = CrawlerProcess(get_project_settings())
        #d = runner.crawl(type, author = author,links = url)
        #dfs.add(d)
        #defer.DeferredList(dfs).addBoth(lambda _: reactor.stop())
        #d.addBoth(lambda _: reactor.stop())
        #reactor.run() # the script will block here until the crawling is finished
       process.crawl(type,author = author,links = url)
       Thread(target=process.start).start()
if __name__ == '__main__':
#sp = SpiderManager()
#urlname = sp.search(type = 'weibo',name = u'JY戴士')
#print(urlname)
#sp.crawl(type = 'weibo',author = u'2',url = urlname)
#urlname = sp.search(type = 'zhihu',name = u'不知所谓')
#sp.crawl(type = 'zhihu',author = u'10',url = urlname)
    sp = SpiderManager()
    urlname = sp.search(type = 'zhihu',name = u'与时间无关的故事')
    sp.crawl(type = 'zhihu',author = '101',url = urlname)
    sp.crawl(type = 'douban',author = '102',url = 'https://www.douban.com/feed/group/rugosarose/discussion')
