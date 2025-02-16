
import multiprocessing
from matplotlib import pyplot
from functools import partial


def square(y,x):
    return x**y

def solve():
    list_range = [i for i in range(10**2)]
    cpus = multiprocessing.cpu_count()
    num_cpus = int(max(1,cpus-1)/2)
    power_max = 4

    for power in range(power_max):
        partial_function = partial(square,power)

        with multiprocessing.Pool(num_cpus) as mp_pool:
            result = mp_pool.map(partial_function,list_range)
            pyplot.plot(result, label="power = : " + str(power))

    pyplot.xlabel('X-axis')
    pyplot.ylabel('Y-axis')
    pyplot.title('Powers')
    pyplot.legend()
    pyplot.show()


if __name__ == "__main__":
    solve()