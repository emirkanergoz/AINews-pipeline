from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    url = Column(Text, nullable=False)
    image = Column(Text, nullable=True)
    source = Column(String(100), default="Webrazzi")
    category = Column(String(100), nullable=True) # İleride AI dolduracak
    sentiment = Column(String(50), nullable=True) # İleride AI dolduracak
    scraped_at = Column(DateTime, default=datetime.utcnow)