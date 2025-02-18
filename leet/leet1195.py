import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.ns = threading.Semaphore(1)
        self.fbs = threading.Semaphore(0)
        self.fs = threading.Semaphore(0)
        self.bs = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):  # alls
            self.ns.acquire()
            if self.isFizzBuzz(i):
                self.fbs.release()
            elif self.isFizz(i):
                self.fs.release()
            elif self.isBuzz(i):
                self.bs.release()
            else:
                printNumber(i)
                self.ns.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):  # fizzbuzz
            if self.isFizzBuzz(i):
                self.fbs.acquire()
                printFizzBuzz()
                self.ns.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):  # fizz
            if self.isFizz(i):
                self.fs.acquire()
                printFizz()
                self.ns.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):  # buzz
            if self.isBuzz(i):
                self.bs.acquire()
                printBuzz()
                self.ns.release()

    def isFizz(self, i):
        return i % 3 == 0 and i % 5 != 0

    def isBuzz(self, i):
        return i % 5 == 0 and i % 3 != 0

    def isFizzBuzz(self, i):
        return i % 3 == 0 and i % 5 == 0
