import threading


def countWorker(num, lock):
    with lock:
        num[0] += 1  # Modify the shared mutable list


def main():
    workers = 5
    num = [0]
    count_lock = threading.Lock()

    print("Before:", num[0])

    worker_threads = [threading.Thread(target=countWorker, args=(num, count_lock)) for _ in range(workers)]

    for thread in worker_threads:
        thread.start()
    for thread in worker_threads:
        thread.join()

    print("After:", num[0])  # Now correctly increments


if __name__ == "__main__":
    main()
