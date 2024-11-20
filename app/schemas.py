from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Схема для регистрации и логина
class UserCreate(BaseModel):
    email: EmailStr # тип данных для проверки, что строка это валидный email
    password: str
    name: str
    age: Optional[int] = None
    interests: Optional[str] = None
    goals: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Схема для запроса
class AdviceRequest(BaseModel):
    user_id: int
    query: str

# Схема для истории запросов
class AdviceResponse(BaseModel):
    id: int
    query: str
    response: str
    timestamp: datetime
    rating: Optional[int] = None

    class Config:
        from_attributes = True
