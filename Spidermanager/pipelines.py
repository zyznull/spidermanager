# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import datetime
import json
import logging
from contextlib import contextmanager

from scrapy import signals
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from Spidermanager.models import db_connect, create_news_table,Article


class ArticleDataBasePipeline(object):
    """保存文章到数据库"""

    def __init__(self):
        engine = db_connect()
        create_news_table(engine)
        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        pass

    def process_item(self, item, spider):
        a = Article(url = item["url"],
                    title = item["title"].encode("utf-8"),
                    topic_id = item["topic_id"],
                    abstract = item["abstract"].encode("utf-8"),
                    publish_time = item["publish_time"].encode("utf-8"))
        session = self.Session()
        b = session.query(Article).filter_by(url = item["url"]).first()
        if(b != None):
            session.delete(b)
            session.commit()
        session.add(a)
        session.commit()
        '''
        with session_scope(self.Session) as session:
            session.add(a)
            session.commit()
        '''

    def close_spider(self, spider):
        pass