from database.redis import redis_client

class RedisModel:

    def __init__(self, name):
        self.name = name
        self.redis = redis_client

    def enqueue(self, item):
        self.redis.rpush(self.name, item)  # Use rpush for FIFO behavior

    def dequeue(self):
        item = self.redis.lpop(self.name)  # Use lpop for FIFO behavior
        return item.decode('utf-8') if item else None
    
    def el_pos(self, value):
        return  self.redis.lpos(name=self.name, value=value)

    def size(self):
        return self.redis.llen(self.name)