from threading import Thread

def slow():
    def check_values_in_list(x):
        for i in range(10**8):
            i in x

    start_time = time.time()
    num_threads = 4
    threads = []
    example_list = [1,2,3,4,5]
    for i in range(num_threads):
        t = Thread(target = check_values_in_list,args=(example_list,))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("diff : ", time.time()-start_time , 'seconds')

import time
import multiprocessing

def check_values_in_list(x):
    for i in range(10 ** 8):
        i in x

def fast():
    start_time = time.time()
    num_processes = 4
    processes = []
    example_list = [1, 2, 3, 4, 5]

    for _ in range(num_processes):
        t = multiprocessing.Process(target=check_values_in_list, args=(example_list,))
        processes.append(t)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("diff:", time.time() - start_time, "seconds")

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")  # ✅ Explicitly set fork on macOS
    # slow() diff 11 seconds
    fast() # diff 3.06 seconds

