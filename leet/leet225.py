class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        top = self.top()
        self.data.pop()
        return top

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

 # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()