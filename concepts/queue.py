
from collections import deque


def appendQExample():
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print('len(queue) : ', len(queue))
    print('pop 1 : ', queue.pop((0)))
    print('len(queue) : ', len(queue))
    print('pop 1 : ', queue.pop((1)))

def getQFromList(nums):
    queue = []
    for i in nums:
        queue.append(i) # O(1)
    return queue

def PopQInOrder(queue):
    while len(queue) > 0:
        # actionables
        queue.pop(0) # O(n)

def getDQFromList(nums):
    q = deque()
    for item in nums:
        q.append(item) # O(1)
    return q

def popDQFromList(q):
    while len(q) > 0:
        # actionables
        q.popleft() # O(1)

nums = [1,2,3]
appendQExample()
queue = getQFromList(nums)
print(queue)
print("popping queue")
PopQInOrder(queue)
print(queue)
dq = getDQFromList(nums)
print(dq)
print("popping deque")
popDQFromList(dq)
print(dq)

# use deque from python collections when dealing with any que like object.
