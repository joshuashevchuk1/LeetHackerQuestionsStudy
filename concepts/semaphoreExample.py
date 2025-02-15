import threading


def semaphoreExample():
    sem1 = threading.Semaphore(1)
    sem2 = threading.Semaphore(0)

    def func1(n):
        sem1.acquire()
        for i in range(n):
            sem1.acquire()
            print("func1", n)
            sem2.release()

    def func2(n):
        for i in range(n):
            sem2.acquire()
            print("func2", n)
            sem1.release()

    t1 = threading.Thread(target=func1, args=(2,))
    t2 = threading.Thread(target=func2, args=(2,))

    t1.start()
    t2.start()

    sem1.release()

    t1.join()
    t2.join()

semaphoreExample()
