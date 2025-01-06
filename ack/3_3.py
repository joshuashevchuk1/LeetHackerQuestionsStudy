class Stack:
    def __init__(self):
        self.stack = []  # Main stack to hold the elements
        self.min_stack = []  # Auxiliary stack to hold the minimum elements

    def push(self, value):
        self.stack.append(value)  # Push to main stack

        # Push the new minimum onto the min_stack
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.is_empty():
            self.min_stack.pop()  # Pop from the min_stack to maintain consistency
            return self.stack.pop()  # Pop from the main stack
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def min(self):
        if not self.is_empty():
            return self.min_stack[-1]  # Return the top of min_stack (O(1))
        return None


# Example usage
stack = Stack()
stack.push(3)
stack.push(1)
stack.push(5)
stack.push(2)

print(stack.min())  # Outputs 1 (minimum element)
stack.pop()
print(stack.min())  # Outputs 1 (minimum element remains same)
stack.pop()
print(stack.min())  # Outputs 1 (minimum element remains same)
stack.pop()
print(stack.min())  # Outputs 3 (minimum element now is 3)
