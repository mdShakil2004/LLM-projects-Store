from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    plan = Column(String, default="free")
    credits = Column(Integer, default=50)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    tokens = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
