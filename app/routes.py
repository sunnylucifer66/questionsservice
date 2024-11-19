from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt # для безопасного хранения пароля(кодируем его)
from app.database import get_db
from app.models import User, Request
from app.schemas import UserCreate, UserLogin, AdviceRequest, AdviceResponse
from g4f.client import Client

router = APIRouter()


# Регистрация пользователя
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first() # аналог чистого SQL запроса - SELECT * FROM users WHERE email = 'user.email' LIMIT 1;
    if existing_user:
        # Если мыло в БД существует - выдаём ошибку
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = bcrypt.hash(user.password) # шифруем пароль
    new_user = User(email=user.email,
                    password=hashed_password,
                    name=user.name,
                    age=user.age,
                    interests=user.interests,
                    goals=user.goals)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


# Авторизация пользователя
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not bcrypt.verify(user.password, db_user.password): # провекряем существует ли пользователь и подходит ли пароль
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": db_user.id}


# Генерация совета
@router.post("/generate_advice")
def generate_advice(request: AdviceRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    prompt = f"Интересы пользователя: {user.interests}, Цели пользователя: {user.goals}. Вопрос: {request.query}"
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    advice = response.choices[0].message.content
    new_request = Request(user_id=user.id, query=request.query, response=advice)
    db.add(new_request)
    db.commit()

    return {"Ответ": advice}


# История запросов
@router.get("/history/{user_id}", response_model=List[AdviceResponse])
def get_history(user_id: int, db: Session = Depends(get_db)):
    history = db.query(Request).filter(Request.user_id == user_id).all()
    return history
