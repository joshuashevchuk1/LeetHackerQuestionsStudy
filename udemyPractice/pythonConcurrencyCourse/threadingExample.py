import threading
import time

result_lock = threading.Lock()

def calc_sum_of_squares(n,sum_squares):
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    n = 5
    sum_squares = 0
    a = threading.Thread(calc_sum_of_squares(n,sum_squares))
    a.run()
    print(a.is_alive())


if __name__ == "__main__":
    main()
    print("starting main")