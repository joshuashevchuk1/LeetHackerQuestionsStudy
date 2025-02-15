import threading

def semaphoreExample():
    sem = threading.Semaphore(2)  # Allowing 2 concurrent accesses

    def func1(n):
        for i in range(n):
            sem.acquire()
            print("func1", n)
            sem.release()

    def func2(n):
        for i in range(n):
            sem.acquire()
            print("func2", n)
            sem.release()

    t1 = threading.Thread(target=func1, args=(2,))
    t2 = threading.Thread(target=func2, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

semaphoreExample()
