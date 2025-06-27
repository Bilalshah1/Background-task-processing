from fastapi import FastAPI, HTTPException
from app.models import Task
import redis
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(REDIS_URL)

@app.post("/enqueue")
async def enqueue(task: Task):
    try:
        r.rpush("task_queue", task.json())
        return {"status": "success", "task": task}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))