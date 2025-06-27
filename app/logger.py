def log_success(task):
    with open("logs.txt", "a") as f:
        f.write(f"SUCCESS: {task}\n")

def log_failure(task, error):
    with open("logs.txt", "a") as f:
        f.write(f"FAILURE: {task} | Error: {error}\n")