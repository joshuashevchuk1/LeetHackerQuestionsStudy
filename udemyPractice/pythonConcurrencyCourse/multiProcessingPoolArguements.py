
import time
import multiprocessing
from matplotlib import pyplot


def square(x):
    return x**2

def solve():
    list_range = [i for i in range(10**6)]
    start_time = time.time()
    cpus = multiprocessing.cpu_count()
    num_cpus = max(1,cpus-1)

    with multiprocessing.Pool(num_cpus) as mp_pool:
        result = mp_pool.map(square,list_range)

    print("diff:", time.time() - start_time, "seconds")
    return result,list_range

def plot():
    result,list_range = solve()
    pyplot.plot(result,label="result")
    pyplot.plot(list_range,label="list_range")
    pyplot.xlabel('X-axis')
    pyplot.ylabel('Y-axis')
    pyplot.title('My Plot')
    pyplot.legend()
    pyplot.show()


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    plot()