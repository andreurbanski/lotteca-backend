import json
import redis

from config.settings import Settings

REDIS = redis.from_url(Settings.REDIS_URL, decode_responses=True)
