from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String(60), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
