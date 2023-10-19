import json
from typing import List

from database.db import init_db, get_session

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Header

from models import Bot
from sqlmodel import Session
from sqlmodel import select, engine, SQLModel

from pydantic import BaseModel, Field




from models import Bot
from bot.service import Service


bot = Bot()
service = Service()

api_routes = APIRouter(
    prefix='/api/bot',
   # tags='API'
)

@api_routes.get('/list')
def get_bots():
    return service.list_bots()

@api_routes.post('/store')
def store_bot(bot: Bot):
    service.set_bot(bot)
    return service.create()
    
@api_routes.get('/start')
def start_bot(id):
    return 'sucess'
    bots = Bot.get_all();
    return json.dumps(bots)

@api_routes.post('/stop')
def stop_bot(id):
    service.set_bot(bot_id=id)
    service.stop_bot()

@api_routes.get('/init_db')
def init_db():
   init_db()