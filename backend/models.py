from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="public")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    category = Column(String)
    description = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    source = Column(String)
    reliability = Column(Float)
    confidence = Column(Float)
    merged_count = Column(Integer, default=1)
    ai_explanation = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
