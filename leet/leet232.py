# solved leet 232

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)  # Removes the first element (FIFO)

    def peek(self) -> int:
        return self.queue[0]  # Returns the front element

    def empty(self) -> bool:
        return len(self.queue) == 0  # Checks if the queue is empty
