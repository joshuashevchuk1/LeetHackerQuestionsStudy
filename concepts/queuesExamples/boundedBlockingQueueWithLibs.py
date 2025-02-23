import queue
import threading
import time

# Create a bounded blocking queue with max size 5
bbq = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        bbq.put(i)  # Blocks if queue is full
        print(f"Produced: {i}")
        time.sleep(0.5)  # Simulate work

def consumer():
    for _ in range(10):
        item = bbq.get()  # Blocks if queue is empty
        print(f"Consumed: {item}")
        bbq.task_done()  # Mark task as done
        time.sleep(1)  # Simulate processing time

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
