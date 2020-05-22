import os
import time

from functions import some_long_function
from redis_resc import redis_queue

while True:
     redis_queue.enqueue(some_long_function, f"This message was queued it {time.time()}")