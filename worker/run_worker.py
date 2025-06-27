import redis
import os
import json
import time
from dotenv import load_dotenv
from app.models import Task
from app.logger import log_success, log_failure

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(REDIS_URL)

def process_task(task: Task):
    if task.type == "send_email":
        print(f"Sending email to {task.payload.get('to')} with subject {task.payload.get('subject')}")
        time.sleep(2)
        return True
    elif task.type == "resize_image":
        print(f"Resizing image to x={task.payload.get('new_x')} y={task.payload.get('new_y')}")
        return True
    elif task.type == "generate_pdf":
        print("Generating PDF...")
        return True
    else:
        print("Unsupported task type")
        return False

if __name__ == "__main__":
    while True:
        job = r.blpop("task_queue", timeout=5)
        if job:
            _, data = job
            task = Task.parse_raw(data)
            success = process_task(task)
            if success:
                log_success(task)
            else:
                log_failure(task, "Failed to process")
        else:
            time.sleep(1)