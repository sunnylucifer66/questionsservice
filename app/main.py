from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.database import engine, Base
from app.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Работает исправно"
