from collections import deque
import sys

def enqueue(q, item):
    q.append(item)

def deQueFront(q):
    q.popleft()

def printFront(q):
    print(q[0])

def queueFromStdin():
    q = deque()
    for line in sys.stdin:
        items = line.split()
        if len(items) > 1:
            if items[0] == '1':
                enqueue(q, items[1])
        else:
            if items[0] == '2':
                deQueFront(q)
            if items[0] == '3':
                printFront(q)
