from collections import deque

class CustomQueue(object):

    def __init__(self):
        self.queue = deque([])

    def enqueue(self, element: int) -> None:
        self.queue.append(element)

    def dequeue(self) -> int:
        return self.queue.pop()

    def size(self) -> int:
        return len(self.queue)

cq = CustomQueue()
cq.enqueue(1)

print(cq.queue)
cq.dequeue()
print(cq.queue)
