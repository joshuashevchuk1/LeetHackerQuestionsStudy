import threading


class Foo:
    def __init__(self):
        self.eventA = threading.Event()
        self.eventB = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.eventA.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.eventA.wait()
        printSecond()
        self.eventB.set()
        self.eventA.clear()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.eventB.wait()
        printThird()
        self.eventB.clear()