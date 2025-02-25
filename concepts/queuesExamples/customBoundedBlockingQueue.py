from collections import deque
import threading
import queue

class BoundedBlockingQueueThreadSafe(object):

    def __init__(self, capacity: int):
        self.queue = queue.Queue()
        self.capacity = threading.Semaphore(capacity)
        self.available = threading.Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.capacity.acquire()
        self.queue.put(element)
        self.available.release()

    def dequeue(self) -> int:
        self.available.acquire()
        item = self.queue.get()
        self.capacity.release()
        return item

    def size(self) -> int:
        return self.queue.qsize()


class CustomBoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque([])
        self.capacity = threading.Semaphore(capacity)
        self.available = threading.Semaphore(0)
        self.mutex = threading.Lock()

    def enqueue(self, element: int) -> None:
        self.capacity.acquire()
        with self.mutex:
            self.queue.append(element)
        self.available.release()

    def dequeue(self) -> int:
        self.available.acquire()
        with self.mutex:
            item = self.queue.popleft()
        self.capacity.release()
        return item

    def size(self) -> int:
        with self.mutex:
            return len(self.queue)


