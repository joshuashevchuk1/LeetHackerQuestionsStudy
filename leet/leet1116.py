# You have a function printNumber that can be called with an integer parameter and prints it to the console.
#
# For example, calling printNumber(7) prints 7 to the console.
# You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd.
#
# The same instance of ZeroEvenOdd will be passed to three different threads:
#
# Thread A: calls zero() that should only output 0's.
# Thread B: calls even() that should only output even numbers.
# Thread C: calls odd() that should only output odd numbers.
# Modify the given class to output the series "010203040506..." where the length of the series must be 2n.
#
# Implement the ZeroEvenOdd class:
#
# ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
# void zero(printNumber) Calls printNumber to output one zero.
# void even(printNumber) Calls printNumber to output one even number.
# void odd(printNumber) Calls printNumber to output one odd number.

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
            printNumber(0)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
           if isEven(i):
                printNumber(self.n)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if isOdd(i):
                    printNumber(i)

def isEven(num):
    if num % 2 == 0:
        return True
    return False

def isOdd(num):
    if num % 2 != 0:
        return True
    return False

def printNumber(x):
    print(x)

n = 0o1021
zeo = ZeroEvenOdd(n)

from threading import Thread

zeroEvenOdd = ZeroEvenOdd(2)

thread_zero = Thread(target=zeroEvenOdd.zero, args=(lambda n: print(n, end=''),))
thread_even = Thread(target=zeroEvenOdd.even, args=(lambda n: print(n, end=''),))
thread_odd = Thread(target=zeroEvenOdd.odd, args=(lambda n: print(n, end=''),))

threads = [thread_zero, thread_even, thread_odd]

for thread in threads:
 thread.start()

for thread in threads:
 thread.join()