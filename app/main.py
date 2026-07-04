# app/main.py

from fastapi import FastAPI
from app.routers import conversation

app = FastAPI(title="Personalized Networking Assistant")

app.include_router(conversation.router)


@app.get("/")
def root():
    return {"message": "Testing Hot Reload"} 