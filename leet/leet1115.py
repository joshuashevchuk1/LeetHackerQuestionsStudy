import threading


class FooBarSemaphore:
    def __init__(self, n):
        self.n = n
        self.f = threading.Semaphore(1)
        self.b = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.f.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.b.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()


class FooBar:
    def __init__(self, n):
        self.n = n
        self.eventA = threading.Event()
        self.eventB = threading.Event()
        self.eventA.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.eventA.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.eventA.clear()
            self.eventB.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.eventB.wait()
            printBar()
            self.eventB.clear()
            self.eventA.set()

def printFoo():
    print("foo")

def printBar():
    print("bar")

n = 5
fooBar = FooBar(n)

t1 = threading.Thread(target = fooBar.foo,args = (printFoo,), daemon=True)
t2 = threading.Thread(target = fooBar.bar,args = (printBar,), daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()