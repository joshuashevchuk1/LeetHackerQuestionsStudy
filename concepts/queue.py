
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
        queue.append(i)
    return queue

def PopQ(queue):
    while len(queue) > 0:
        # actionables
        queue.pop(0)

nums = [1,2,3]
appendQExample()
queue = getQFromList(nums)
print(queue)
print("popping queue")
PopQ(queue)
print(queue)