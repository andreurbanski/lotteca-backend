import logging

from database.db import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


#from app.config.settings import settings
from api.routes import api_routes

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_routes)

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}