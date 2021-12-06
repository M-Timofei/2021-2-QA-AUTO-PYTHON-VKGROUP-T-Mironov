from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
    Request = Column(String(1000), nullable=False)
    Count = Column(Integer, nullable=False)

class TopURL(Base):

    __tablename__ = 'Top_URL'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests_by_type(" \
               f"id='{self.id}'," \
               f"URL='{self.URL}'," \
               f"Count='{self.Count}' " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    URL = Column(String(1000), nullable=False)
    Count = Column(Integer, nullable=False)

class Top_4XX(Base):
    __tablename__ = 'Top_4XX_errors'
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
    URL = Column(String(1000), nullable=False)
    Response = Column(Integer, nullable=False)
    Size = Column(Integer, nullable=False)
    IP = Column(String(30), nullable=False)

class Top_5XX(Base):
    __tablename__ = 'Top_5XX_errors'
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