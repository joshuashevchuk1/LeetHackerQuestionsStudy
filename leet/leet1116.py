import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroS = threading.Semaphore(1)
        self.evenS = threading.Semaphore(0)
        self.oddS = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range (self.n):
            self.zeroS.acquire()
            printNumber(0)
            if isEven(i):
                self.oddS.release()
            elif isOdd(i):
                self.evenS.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
           self.evenS.acquire()
           printNumber(i)
           self.zeroS.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddS.acquire()
            printNumber(i)
            self.zeroS.release()

def isEven(num):
    if num % 2 == 0:
        return True
    return False

def isOdd(num):
    if num % 2 != 0:
        return True
    return False