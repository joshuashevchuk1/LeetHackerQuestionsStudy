import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.eventA = threading.Event()
        self.eventB = threading.Event()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        self.eventA.set()
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
        self.eventA.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        self.eventB.set()
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
        self.eventB.wait()
        self.eventA.clear()
        self.eventB.clear()

def printFoo():
    print("foo")

def printBar():
    print("bar")

n = 5
fooBar = FooBar(5)