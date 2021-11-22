from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from utils.script import max_len_top_10, max_len_requests_by_type, max_len_URL_4XX

Base = declarative_base()

class TotalRequests(Base):
    __tablename__ = 'Total_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total_requests(" \
               f"id='{self.id}'," \
               f"Count='{self.Count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Count = Column(Integer, nullable=False)

class RequestsByType(Base):
    __tablename__ = 'Requests_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests_by_type(" \
               f"id='{self.id}'," \
               f"Request='{self.Request}'," \
               f"Count='{self.Count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Request = Column(String(max_len_requests_by_type), nullable=False)
    Count = Column(Integer, nullable=False)

class Top10URL(Base):
    __tablename__ = 'Top_10_URL'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests_by_type(" \
               f"id='{self.id}'," \
               f"URL='{self.URL}'," \
               f"Count='{self.Count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    URL = Column(String(max_len_top_10), nullable=False)
    Count = Column(Integer, nullable=False)

class Top5_4XX(Base):
    __tablename__ = 'Top_5_4XX_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests_by_type(" \
               f"id='{self.id}'," \
               f"URL='{self.URL}'," \
               f"Response='{self.Response}', " \
               f"Size='{self.Size}', "\
               f"IP='{self.IP}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    URL = Column(String(max_len_URL_4XX), nullable=False)
    Response = Column(Integer, nullable=False)
    Size = Column(Integer, nullable=False)
    IP = Column(String(30), nullable=False)

class Top5_5XX(Base):
    __tablename__ = 'Top_5_5XX_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests_by_type(" \
               f"id='{self.id}'," \
               f"IP='{self.IP}'," \
               f"Count='{self.Count}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    IP = Column(String(30), nullable=False)
    Count = Column(Integer, nullable=False)