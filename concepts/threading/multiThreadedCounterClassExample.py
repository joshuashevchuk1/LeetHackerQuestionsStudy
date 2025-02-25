
import threading

class MultiThreadedCount:
    def __init__(self):
        pass

class MultiThreadedWorker(threading.Thread):
    def __init__(self,nums, lock, **kwargs):
        super(MultiThreadedWorker,self).__init__(**kwargs)
        self.nums = nums
        self.lock = lock

    def count(self):
        with self.lock:
            self.nums[0] += 1

    def run(self):
        self.count()


