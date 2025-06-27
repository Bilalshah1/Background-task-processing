# Distributed Background Task Queue in Python

A scalable, modular background job processing system built with **FastAPI** and **Redis**. Offload time-consuming tasks (like sending emails, image processing, or PDF generation) from your main application for a faster, more responsive user experience.

---

## 🚀 Features
- **RESTful API** for enqueuing jobs (`/enqueue`)
- **Redis-backed queue** for reliable job storage
- **Worker service** for concurrent, asynchronous task execution
- **Live metrics endpoint** (`/metrics`) for monitoring
- **Simple logging** to `logs.txt` for traceability
- **Easily extensible**: add your own job types with minimal code

---

## 🏗️ Architecture

```
Client → [FastAPI Producer] → [Redis Queue] ← [Worker Service]
                                         ↓
                                    [logs.txt]
```
- **Client**: Sends HTTP POST requests to enqueue jobs
- **Producer (API)**: Receives jobs and enqueues them in Redis
- **Redis**: Stores jobs until processed
- **Worker**: Dequeues and processes jobs, logs results, exposes `/metrics`

---

## ⚡ Example Use Case
When a user signs up, your app can POST a job to `/enqueue` to send a welcome email. The user gets an instant response, while the email is sent in the background by the worker.

---

## 🛠️ Setup & Installation

1. **Clone the repository**
2. **Install Redis** (if not already running)
   ```bash
   sudo apt update && sudo apt install redis-server
   redis-server
   ```
3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment**
   - Create a `.env` file:
     ```
     REDIS_URL=redis://localhost:6379/0
     ```

---

## 🚦 Running the System

1. **Start the Producer API**
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Start the Worker**
   ```bash
   python -m worker.run_worker
   ```

---

## 📬 Enqueue a Job (API Example)

Send a POST request to `/enqueue`:
```json
{
  "type": "send_email",
  "payload": {
    "to": "user@example.com",
    "subject": "Welcome!"
  },
  "retries": 3
}
```
**Curl Example:**
```bash
curl -X POST "http://127.0.0.1:8000/enqueue" -H "Content-Type: application/json" -d '{"type":"send_email","payload":{"to":"user@example.com","subject":"Welcome!"},"retries":3}'
```

---

## 📊 Get Metrics

Check worker stats at:
```
GET http://127.0.0.1:8001/metrics
```

---

## 🧩 Extending the System
- Add new job types by editing the `process_task` function in `worker/run_worker.py`.
- Add your logic under a new `if` or `elif` block for your custom task type.

---

## 👤 Credits
Developed by [BilalShah+Cursor]. Inspired by distributed systems best practices. 
