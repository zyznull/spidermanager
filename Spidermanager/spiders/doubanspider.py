from scrapy.spiders import XMLFeedSpider
from Spidermanager.items import ArticleItem
class doubanSpider(XMLFeedSpider):
    name = 'douban'
    start_urls = []

    def __init__(self,author,links,*args,**kwargs):
        super(doubanSpider,self).__init__(*args,**kwargs)
        self.author = author
        self.start_urls.append(links)

    def parse_node(self, response, selector):
        items = selector.xpath("/rss/channel/item")
        for ele in items:
            item = ArticleItem()
            item['link'] = str(ele.xpath("link/text()")[0].extract())
            item['title'] = str(ele.xpath("title/text()")[0].extract())
            item['author'] = self.author
            item['desc'] = str(ele.xpath("description/text()")[0].extract())
            yield item