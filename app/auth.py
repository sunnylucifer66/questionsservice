from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.models import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import Header, Depends
from app.database import get_db


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise JWTError("User ID not found")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise JWTError("User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def get_current_user(
    token: str = Header(..., alias="Authorization"),
    db: Session = Depends(get_db)):
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = token.split("Bearer ")[1]
    return verify_token(token, db)
