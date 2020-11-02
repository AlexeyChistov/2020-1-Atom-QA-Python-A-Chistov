from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from log_maker.log_maker import LogMaker

Base = declarative_base()


class Model(Base, LogMaker):
    __tablename__ = 'table_orm_sql'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)
    date = Column(DateTime, nullable=False)
    method = Column(String(10), nullable=False)
    url = Column(String(255), nullable=False)
    resp_code = Column(Integer, nullable=False)

    def __init__(self, ip, date, method, url, resp_code):
        self.ip = ip
        self.date = date
        self.method = method
        self.url = url
        self.resp_code = resp_code

    def __repr__(self):
        return "Log (" \
               f"id = {self.id}, " \
               f"ip = {self.ip}, " \
               f"date = {self.date}, " \
               f"method = {self.method}, " \
               f"url = {self.url}, " \
               f"resp_code = {self.resp_code});"
