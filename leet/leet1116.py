import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroS = threading.Semaphore(1)
        self.evenS = threading.Semaphore(0)
        self.oddS = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range (self.n): # alls
            self.zeroS.acquire()
            printNumber(0)
            if isEven(i):
                self.oddS.release()
            elif isOdd(i):
                self.evenS.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2): # evens
           self.evenS.acquire()
           printNumber(i)
           self.zeroS.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2): # odds
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

class ZeroEvenOddFaster:
    def __init__(self, n):
        self.n = n
        self.z = threading.Lock()  # Using Lock instead of Semaphore(1)
        self.e = threading.Semaphore(0)
        self.o = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.e.release()
            else:
                self.o.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()
