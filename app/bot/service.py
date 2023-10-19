from bot.repository import Repository
from config.initializers import REDIS
from models import Bot
from sqlmodel import Session
from database.db import engine

from tasks.client import enqueue, kill




class Service:

    strategies = dict()
    pid = 0
    score = 0
    redis = REDIS
    #singleton
    bot = Bot()
    session = Session(engine)
    repository = Repository()


    def __init__(self, id=None) -> None:
        #self.bot = self.repository.getBotById(id)
        return

    def run(self):
        for strategy in self.bot.config.strategies:
            try:
                enqueue(type='strategies', name={strategy.name}, target_id=Bot.id)
            except Exception:
                print(f"Error starting the strategy {strategy.name}.")

    def stop_bot(self):
        kill()

    def refresh_data(self):
        self.redis[self.bot.id]['data'] = self.operation.acquire_data();

    def get_score(self):
        score = 0
        for pid in self.redis[self.bot.id]['strategy'] :
              score += self.redis[self.bot.id][pid]['score']
        
        self.redis[self.bot.id]['score'] = score

    def create(self):
        self.session.add(self.bot)
        self.session.commit()
        self.session.close()
        return self.bot

    def get(self):
        return {}
    
    def list_bots(self):
        botList = self.repository.getBotsByUser(1)
        return botList
    
    def set_bot(self, bot: Bot=None, bot_id: int = None):
        
        if bot_id is not None:
            bot = Repository.getBotById(bot_id)
        self.bot = bot
        return bot
        
