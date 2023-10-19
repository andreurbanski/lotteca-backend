from database.redis.queue import Queue
import uuid


task_running = Queue(name='pending_tasks')
task_kill = Queue(name='kill_tasks')

def kill(id):
    task_kill.enqueue(id)

def enqueue(type, name, target_id):
    task_id = uuid.uuid4()
    task_running.enqueue(f'{"type":"{type}","name":"{name}","target_id": {target_id}, "task_id": {task_id}}')

    return task_id