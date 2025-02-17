import threading

class SemaphoreDual():
    def __init__(self):
        self.semH = threading.Semaphore(2)
        self.semO = threading.Semaphore(0)
        self.mutex = threading.Lock()
        self.h_count = 0

    def hydrogen(self):
        self.semH.acquire()
        print("H")
        self.semO.release()

    def oxygen(self):
        self.semO.acquire()
        print("O")
        self.semH.release()
        self.semH.release()

def semaphoreExampleDual():

    h = 4

    threads = []

    semaphoreDual = SemaphoreDual()

    for i in range(h):
        threads.append(threading.Thread(target=semaphoreDual.hydrogen))

    o = 2
    for i in range(o):
        threads.append(threading.Thread(target=semaphoreDual.oxygen))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

semaphoreExampleDual()
