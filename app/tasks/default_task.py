import os
import time
from database.redis.queue import Queue

class DefaultTask:
    task_id = None
    task_status = 0
    loop_wait = 5 # seconds - Overide by child module
    stop_tasks = Queue(name='stop_tasks')

    def __init__(self) -> None:
        pass
    
   
    def start(self):
        while not self.stop():
            self.run()
            time.sleep(self.loop_wait)
        
    
    def stop(self):
        if self.stop_tasks.el_pos(self.task_id) is not None:
            return True
        return False
    