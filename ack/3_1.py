
from collections import deque


class Stack:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.stack = deque(array)

array = [1,2,3,4]
s1 = Stack(array)
s2 = Stack(array)
s3 = Stack(array)