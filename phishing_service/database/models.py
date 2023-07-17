from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PhishingURL modeli tanımı
class PhishingURL(Base):
    __tablename__ = "phishing_urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    fetched_date = Column(DateTime)
    source = Column(String)

    def __init__(self, url, fetched_date, source):
        self.url = url
        self.fetched_date = fetched_date
        self.source = source
