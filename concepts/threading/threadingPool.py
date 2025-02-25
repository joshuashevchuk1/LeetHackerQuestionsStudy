import concurrent.futures
import threading

global n

def task(n,lock):
    with lock:
        print(n*2)

def main():

    n = 2
    mutex = threading.Lock()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exec:
        exec.map(task(n,mutex),range(3))

    print(n)

if __name__ == "__main__":
    main()