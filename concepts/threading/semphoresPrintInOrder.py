import threading

class Foo:
    def __init__(self):
        self.f1 = threading.Semaphore(1)
        self.f2 = threading.Semaphore(0)
        self.f3 = threading.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.f1.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f2.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.f2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.f3.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.f3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.f1.release()