import threading
import time

result_lock = threading.Lock()

def calc_sum_of_squares(n,sum_squares):
    with result_lock:
        for i in range(n):
            sum_squares += i ** 2
        print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    start = time.time()
    n = 100000
    sum_squares = 0
    a = threading.Thread(target=calc_sum_of_squares, args=(n, sum_squares))
    a.start()
    finish = time.time()
    print(abs(start-finish))


if __name__ == "__main__":
    main()
    print("starting main")