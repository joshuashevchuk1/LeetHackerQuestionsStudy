import threading

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

n = 5
for i in range(n):
    t1 = threading.Thread(target=func1, args=(1,))
    t2 = threading.Thread(target=func2, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
