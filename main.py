import os
import time

import redis
from functions import some_long_function
from rq import Queue

redis_conn = redis.Redis(
     host=os.getenv("REDIS_HOST", "127.0.0.1"),
     port=os.getenv("REDIS_PORT", "6379"),
     password=os.getenv("REDIS_PASSWORD", "")
)

redis_queue = Queue(connection=redis_conn)

job = redis_queue.enqueue(some_long_function, "Hello World!")

while True:
     if job.result:
          print(job.result)
          break
