
import time
import multiprocessing

def check_values_in_list(x,i,nump,queue): # by splitting up the process we significantly reduce the time to search
    max_number = 10**8
    lower = int(i * max_number/nump)
    upper = int((i+1) * max_number/nump)
    hits = 0
    for i in range(lower,upper):
        if i in x:
            hits += 1

    queue.put((lower,upper,hits))

def fastest():
    start_time = time.time()
    num_processes = 4
    processes = []
    example_list = [1, 2, 3, 4, 5]
    queue = multiprocessing.Queue()

    for i in range(num_processes):
        t = multiprocessing.Process(target=check_values_in_list, args=(example_list,i,num_processes,queue))
        processes.append(t)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    queue.put("DONE")

    while True:
        v =  queue.get()
        if v == "DONE":
            break
        lower,upper,hits = v
        print('Between ', lower,'and ',upper,'with hits : ', hits)

    print("diff:", time.time() - start_time, "seconds")

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")  # Explicitly set fork on macOS
    fastest() # diff 0.76 seconds