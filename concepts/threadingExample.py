import concurrent.futures
import threading
import time

limit = 100000


def exampleA():
    """
    This method manually creates and manages threads. Although it involves thread management overhead,
    the simplicity of the thread logic and minimal additional scheduling overhead leads to the fastest execution
    in this specific case.

    Pros:
    ✅ Simple thread creation with minimal overhead from function calls.
    ✅ Threads do independent work with minimal contention, and the computation is CPU-heavy.

    Cons:
    ❌ Manually managing threads introduces slight overhead, particularly as the number of threads increases.
    ❌ Still affected by Python’s Global Interpreter Lock (GIL), limiting true parallelism.
    """

    def calc_sum_of_squares(n):
        sum_squares = 0
        for i in range(n):
            sum_squares += i ** 2

    def main():
        threads = []
        start = time.time()
        for i in range(5):
            max_value = (i + 1) * limit
            t = threading.Thread(target=calc_sum_of_squares, args=(max_value,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        finish = time.time()
        print(f"Total execution time ExampleA: {finish - start:.4f} seconds")

    main()


def exampleC():
    """
    This method is the slowest due to the unnecessary function call overhead in the loop.
    Each thread calls `calc_sum()` on every iteration, leading to increased memory usage
    and higher execution time.

    Pros:
    ✅ Uses multiple threads, but the computation could be more efficient if handled directly.

    Cons:
    ❌ Function call overhead from `calc_sum()` is unnecessary and adds significant cost.
    ❌ Increased memory usage due to the passing and returning of values on each iteration.
    ❌ Slower execution time due to the excessive overhead compared to Examples A and B.
    """

    def calc_sum_of_squares(n):
        sum_squares = 0
        for i in range(n):
            sum_squares = calc_sum(sum_squares, i)

    def calc_sum(sum_squares, i):
        sum_squares += i ** 2
        return sum_squares

    def main():
        threads = []
        start = time.time()
        for i in range(5):
            max_value = (i + 1) * limit
            t = threading.Thread(target=calc_sum_of_squares, args=(max_value,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        finish = time.time()
        print(f"Total execution time ExampleC: {finish - start:.4f} seconds")

    main()


def exampleB():
    """
    This method uses a `ThreadPoolExecutor`, which reduces overhead by reusing threads.
    However, it introduces some scheduling overhead, making it slightly slower than Example A in this case.

    Pros:
    ✅ Reduces thread creation and destruction overhead with a thread pool.
    ✅ Efficient thread management through `ThreadPoolExecutor`.

    Cons:
    ❌ Still affected by Python’s Global Interpreter Lock (GIL), limiting true parallelism.
    ❌ The scheduling and management overhead of `ThreadPoolExecutor` leads to slightly slower execution than Example A in this case.
    """

    def calc_sum_of_squares(n):
        return sum(i ** 2 for i in range(n))

    def main():
        start = time.time()
        max_values = [(i + 1) * limit for i in range(5)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(calc_sum_of_squares, max_values)

        finish = time.time()
        print(f"Total execution time ExampleB: {finish - start:.4f} seconds")

    main()


if __name__ == "__main__":
    exampleA()
    exampleB()
    exampleC()
    print("starting main")
