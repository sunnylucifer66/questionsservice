from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False) # unique=True(Уникальные значения, например: 2 польз. не могут иметь одинаковую почту)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    interests = Column(String, nullable=True)
    goals = Column(String, nullable=True)

    requests = relationship("Request", back_populates="user") # связь 1 ко многим


class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # ForeignKey("users.id") указывает на конкретного пользователя
    query = Column(String, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=func.now()) # Генерим текущую дату и время
    rating = Column(Integer, nullable=True)

    user = relationship("User", back_populates="requests") # связь многие к 1
