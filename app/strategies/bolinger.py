from strategies.default_strategy import DefaultStrategy
import random

class_name = 'Bolinger'

class Bolinger(DefaultStrategy):
    
    score:int = 0
    name = "Bolinger"

    def __init__(self, bot_id, task_id) -> None:
        self.load(bot_id, task_id)
        print('Loaded data from Redis')

    def calculate(self):
        self.score = random.uniform(-4.0, 4.0)
        print(f"Calculated Score for bot  bunda {self.bot.id} - {self.name}: {self.score}" )