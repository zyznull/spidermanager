import requests
import scrapy

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

def search(name):
    url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query='+name
    html = requests.get(url,headers = header)
    selecter = scrapy.selector.Selector(text = html.content.decode())
    linkname = selecter.xpath('//div[@id="main"]/div[@class="news-box"]/ul/li/div/div[@class="txt-box"]/p/a/em/text()').extract_first()
    if linkname == name:
        return linkname
    return ''


