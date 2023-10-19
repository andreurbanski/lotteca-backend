from bot.repository import Repository
from tasks.default_task import DefaultTask
from models import Bot
from database.redis.list import List



class DefaultStrategy(DefaultTask):
    bot:Bot = None
    botRepo = Repository()
    result_list = List(f"")
    
    def load(self, bot_id, task_id):
        self.bot = self.botRepo.getBotById(bot_id)
        self.config = self.bot.config
        self.task_id =  task_id

    def run(self):
        self.calculate()

    def store_results(self):
        pass



   

