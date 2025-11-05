import os
import redis
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = int(os.getenv('REDIS_PORT', 6379))
        self.password = os.getenv('REDIS_PASSWORD', None)
        self.db = int(os.getenv('REDIS_DB', 0))

    def get_connection(self):
        return redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db,
            decode_responses=True
        )

if __name__ == "__main__":
    config = RedisConfig()
    redis_conn = config.get_connection()
    redis_conn.set('test_key', 'test_value')
    print(redis_conn.get('test_key'))