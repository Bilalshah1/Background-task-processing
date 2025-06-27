from pydantic import BaseModel
from typing import Dict, Any

class Task(BaseModel):
    type: str
    payload: Dict[str, Any]
    retries: int = 0

class Metrics(BaseModel):
    total_jobs_in_queue: int = 0
    jobs_done: int = 0
    jobs_failed: int = 0