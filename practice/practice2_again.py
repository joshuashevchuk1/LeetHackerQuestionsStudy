import threading


class EventProcessor:
    def __init__(self):
        self.event_A = threading.Event()
        self.event_B = threading.Event()

    def eventAProcess(self):
        for i in range(25):
            self.event_A.set()
            print("Subsystem A: Log generated")

    def eventBProcess(self):
        for i in range(25):
            self.event_A.wait()
            print("Subsystem B: Log generated")
            self.event_B.set()
            self.event_A.clear()

    def eventCProcess(self):
        for i in range(25):
            self.event_B.wait()
            print("Subsystem C: Log generated")
            self.event_B.clear()


eventProc = EventProcessor()

threadA = threading.Thread(target=eventProc.eventAProcess, daemon=True)
threadB = threading.Thread(target=eventProc.eventBProcess, daemon=True)
threadC = threading.Thread(target=eventProc.eventCProcess, daemon=True)

threadA.start()
threadB.start()
threadC.start()

threadA.join()
threadB.join()
threadC.join()
