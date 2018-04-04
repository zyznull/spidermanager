from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Article(Base):
    """电子邮件表"""
    __tablename__ = 'Article'
    title = Column(String(100), primary_key=True)
    url = Column(Text(500), index = True,unique = True,nullable=False)
    abstract = Column(Text(500),unique = False)
    topic_id = Column(Integer,index = True,unique = False)
    publish_time = Column(String(51),index = False,unique = False)
    def __repr__(self):
        return "<Article(link='{}')>".format(self.link)

def db_connect():
    return create_engine('mysql+pymysql://root:cptbtptp@127.0.0.1:3306/spider', echo=True)

def create_news_table(engine):
    Base.metadata.create_all(engine)



