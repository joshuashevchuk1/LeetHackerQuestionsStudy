import threading
import time
import random


class LogProcessor:
    def __init__(self):
        self.semA = threading.Semaphore(1)
        self.semB = threading.Semaphore(0)
        self.semC = threading.Semaphore(0)

    def sleepRandom(self):
        time.sleep(1)

    def process_A(self):
        while True:
            self.semA.acquire()
            time.sleep(1)
            print("Subsystem A: Log generated")
            self.semB.release()

    def process_B(self):
        while True:
            self.semB.acquire()
            time.sleep(1)
            print("Subsystem B: Log generated")
            self.semC.release()

    def process_C(self):
        while True:
            self.semC.acquire()
            time.sleep(1)
            print("Subsystem C: Log generated\n")
            self.semA.release()



if __name__ == "__main__":
    log_processor = LogProcessor()

    # Creating and starting threads
    thread_A = threading.Thread(target=log_processor.process_A, daemon=True)
    thread_B = threading.Thread(target=log_processor.process_B, daemon=True)
    thread_C = threading.Thread(target=log_processor.process_C, daemon=True)

    thread_A.start()
    thread_B.start()
    thread_C.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)
