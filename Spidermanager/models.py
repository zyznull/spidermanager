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
    link = Column(String(500), index = True,nullable=False)
    desc = Column(String(500),unique = False)
    author = Column(String(100),index = True,unique = False)
    def __repr__(self):
        return "<Article(link='{}')>".format(self.link)

def db_connect():
    return create_engine('mysql+pymysql://root:cptbtptp@127.0.0.1:3306/spider', echo=True)

def create_news_table(engine):
    Base.metadata.create_all(engine)



