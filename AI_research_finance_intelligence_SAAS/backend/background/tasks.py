import time

def long_task(prompt: str):
    time.sleep(5)
    return f"Processed: {prompt}"
