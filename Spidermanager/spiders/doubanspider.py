from scrapy.spiders import XMLFeedSpider
from Spidermanager.items import ArticleItem
import datetime
class doubanSpider(XMLFeedSpider):
    name = 'douban'
    start_urls = []

    def __init__(self,author,links,*args,**kwargs):
        super(doubanSpider,self).__init__(*args,**kwargs)
        self.author = int(author)
        self.start_urls.append(links)

    def parse_node(self, response, selector):
        items = selector.xpath("/rss/channel/item")
        for ele in items:
            item = ArticleItem()
            item['url'] = str(ele.xpath("link/text()")[0].extract())
            item['title'] = str(ele.xpath("title/text()")[0].extract())
            item['topic_id'] = self.author
            item['abstract'] = str(ele.xpath("description/text()")[0].extract())
            item['publish_time'] = datetime.datetime.now()
            yield item