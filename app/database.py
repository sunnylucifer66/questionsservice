from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./generator.db" # создаём файлик БД

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # check_same_thread = False - разрешает многопоток
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # управляем комитами и синхронизациями самостоятельно

Base = declarative_base()

# Подключаемся к БДшке
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()