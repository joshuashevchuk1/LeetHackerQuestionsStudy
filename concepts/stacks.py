
# stack from a list
class Stack:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.stack = array  # Start with an existing array or an empty one

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def min(self):
        return min(self.stack)