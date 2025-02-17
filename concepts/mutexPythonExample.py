import threading

n = 0  # Initialize n globally
mutex = threading.Lock()  # Create a shared mutex

class Worker(threading.Thread):
    def __init__(self,k, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.k = k
        self.start()

    def add_n(self):
        global n
        with mutex:
            for i in range(self.k):# Use `with` to handle locks safely
                n += 1

    def run(self):
        self.add_n()


threads = []
k=5

for i in range(1):
    t = Worker(k)
    threads.append(t)

for t in threads:
    t.join()

print(n)  # Expected output: 2
