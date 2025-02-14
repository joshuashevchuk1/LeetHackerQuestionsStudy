import threading

from leet.solve_me.leet323 import array


# we want to iterate over an array and split the len of the array into pieces

class Worker(threading.Thread):
    def __init__(self, n, **kwargs):
        self.n = None
        super(Worker, self).__init__(**kwargs)
        self.start()


def getMultipleArray(n):
    array = [0] * (n+1)
    return array

def getThreadBatchs(n):
    array = getMultipleArray(n)
    window = 0






