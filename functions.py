import time

from rq import get_current_job


def some_long_function(some_input):
        job = get_current_job()
        time.sleep(10)
        return {
            "job_id": job.id,
            "result": some_input
        }
