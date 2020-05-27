import os
import time

from flask import Flask, jsonify, request
from functions import some_long_function
from redis_resc import redis_queue, redis_conn
from rq.job import Job

app = Flask(__name__)

@app.route("/")
def home():
     return "Running!"

@app.route("/enqueue")
def enqueue():
     job = redis_queue.enqueue(some_long_function, f"This message was queued it {time.time()}")
     return jsonify({
          "job_id": job.id
     })

@app.route("/check_status")
def check_status():
     job_id = request.args["job_id"]
     job = Job.fetch(job_id, connection=redis_conn)
     return jsonify({
          "job_id": job.id,
          "job_status": job.get_status()
     })

if  __name__ == "__main__":
     app.run(debug=True)
