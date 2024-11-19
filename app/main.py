from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Привет, каким советом я могу тебе помочь? :)"}
