import threading

class WorkerExample(threading.Thread):
    def __init__(self,**kwargs):
        super(WorkerExample,self).__init__(**kwargs)
        self.start()

    def run(self):
        print("foo")


class WorkerExample2(threading.Thread):
    def __init__(self, **kwargs):
        super(WorkerExample2, self).__init__(**kwargs)
        self.start()

    def run(self):
        print("bar")

for i in range(100):
    w = WorkerExample()
    w2 = WorkerExample2()
    w.join()
    w2.join()
