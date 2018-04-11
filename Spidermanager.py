from scrapy import cmdline
from search import *
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

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
        runner = CrawlerRunner(get_project_settings())
        # 'followall' is the name of one of the spiders of the project.
        d = runner.crawl(type, author = author,links = url)
        d.addBoth(lambda _: reactor.stop())
        reactor.run() # the script will block here until the crawling is finished
sp = SpiderManager()
urlname = sp.search(type = 'zhihu',name = u'金与火之歌')
print(urlname)
sp.crawl(type = 'zhihu',author = u'1',url = urlname)

