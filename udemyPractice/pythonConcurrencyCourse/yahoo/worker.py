import threading
import time


class Worker(threading.Thread):
    def __init__(self, n, **kwargs):
        self.n = n
        super(Worker, self).__init__(**kwargs)
        self.start()

    def calc_sum_of_squares(self):
        sum_squares = 0
        for i in range(self.n):
            sum_squares += i ** 2

    def run(self):
        self.calc_sum_of_squares()


def main():
    limit = 10000
    start = time.time()
    threads = []
    for i in range(5):
        max_value = (i + 1) * limit
        w = Worker(max_value)
        threads.append(w)

    for thread in threads:
        thread.join()
    end = time.time()
    print(abs(end-start))

if __name__== "__main__":
    main()