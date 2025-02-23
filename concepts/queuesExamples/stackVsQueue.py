from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # 3 (Last in, first out)
print(stack.pop())  # 2
print(stack.pop())  # 1

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())  # 1 (First in, first out)
print(queue.popleft())  # 2
print(queue.popleft())  # 3
