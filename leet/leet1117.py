import threading

class H2O:
    def __init__(self):
        self.h = threading.Semaphore(2)
        self.o = threading.Semaphore(0)
        self.mutex = threading.Lock()
        self.h_count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h.acquire()
        releaseHydrogen()
        with self.mutex:
            self.h_count += 1
            if self.h_count == 2:
                self.o.release()
                self.h_count = 0

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.acquire()
        releaseOxygen()
        self.h.release()
        self.h.release()