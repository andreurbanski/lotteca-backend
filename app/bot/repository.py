from database.db import Session, engine
from config.initializers import REDIS
from models import Bot
from sqlmodel import select, SQLModel
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import NoResultFound



class Repository:
    #singleton
    bot = Bot()
    session = Session(engine)

    def __init__(self) -> None:
        return

    def getBotsByUser(self, logged_user):
        data = []
        bots = self.session.query(Bot).options(selectinload(Bot.asset)).all()

        for bot in bots:

            bot_data = {
                    'bot_id': bot.id,
                    'status': bot.status,
                    'assets': [
                        {
                            'id': bot.asset.id,
                            'name': bot.asset.name,
                        }
                    ]
                }
            data.append(bot_data)

        
    
        return  data
    
    def getBotById(self, bot_id=1):
        try:
            bot = self.session.query(Bot).filter(Bot.id == bot_id).one()
            return bot
        except Exception as e:
            raise e #ValueError(f"Bot with id {bot_id} not found")
