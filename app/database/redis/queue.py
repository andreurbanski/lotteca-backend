from database.redis.redis_model import RedisModel

class Queue(RedisModel):

    def enqueue(self, item):
        self.redis.rpush(self.name, item)  # Use rpush for FIFO behavior

    def dequeue(self):
        item = self.redis.lpop(self.name)  # Use lpop for FIFO behavior
        return item.decode('utf-8') if item else None
    
    def el_pos(self, value):
        return  self.redis.lpos(name=self.name, value=value)

    def size(self):
        return self.redis.llen(self.name)