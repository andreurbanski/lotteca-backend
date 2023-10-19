from database.redis.redis_model import RedisModel

class List(RedisModel):

    def push(self, key, *values):
        return self.redis.rpush(self.name, *values)

    def get(self, key, start=0, end=-1):
        return self.redis.lrange(self.name, start, end)

    def remove(self, key, value, count=0):
        return self.redis.lrem(self.name, count, value)
    
    def el_pos(self, value):
        return  self.redis.lpos(name=self.name, value=value)

    def size(self):
        return self.redis.llen(self.name)