import threading
import queue
import time

# Shared queue
q = queue.Queue()

def producer():
    """ Produces items and adds them to the queue """
    for i in range(10):
        item = f"Item-{i}"
        q.put(item)  # Thread-safe operation
        print(f"Produced: {item}")
        time.sleep(0.5)  # Simulate production delay
    q.put(None)  # Sentinel value to signal consumer to stop

def consumer():
    """ Consumes items from the queue """
    while True:
        item = q.get()
        if item is None:
            break  # Exit on sentinel value
        print(f"Consumed: {item}")
        time.sleep(1)  # Simulate processing delay
        q.task_done()

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for completion
producer_thread.join()
consumer_thread.join()

print("Threading-based processing complete.")
