
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

# poping a stack with mutliple entries

def popBigStack():
    stack = []
    current_string = "a"
    stack.append((current_string,3))
    print(stack)
    current_string += "b"
    stack.append((current_string,3))
    print(stack)
    current_string += "c"
    stack.append((current_string, 3))
    print(stack)
    last_string, multiplier = stack.pop()
    print(last_string, multiplier)

popBigStack()