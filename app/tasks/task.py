from celery import Celery
from database.redis.queue import Queue
from database.redis.list import List

import importlib 
import time
import json

taskman = Celery('tasks', broker='redis://localhost:6379/0')
task_queue = Queue(name='pending_tasks')
task_running = List(name='running_tasks')



@taskman.task
def init_task(task_type, task_name, target_id, task_id):

   # try:
        module_import =  importlib.import_module(f"{task_type}.{task_name}")
        klass = getattr(module_import, getattr(module_import, 'class_name'))
        module = klass(target_id, task_id)
        module.start()
        print(f'Module {task_name} target {target_id} started')
    #except Exception as e:
    #        print(f"Error importing the task {task_type} {task_name}.")
    #        print(e)


@taskman.task
def task_handler():
        while True:
            while task_queue.size() > 0:
                task = json.loads(task_queue.dequeue())
                init_task.delay(task['type'], task['name'], task['target_id'], task['task_id'])

            time.sleep(2)

