import threading
import time
import random


class LogProcessor:
    def __init__(self):
        self.event_A_done = threading.Event()
        self.event_B_done = threading.Event()

    def process_A(self):
        while True:
            time.sleep(random.uniform(0.5, 1.5))  # Simulate log generation
            print("Subsystem A: Log generated")
            self.event_A_done.set()  # Signal B to start

    def process_B(self):
        while True:
            self.event_A_done.wait()  # Wait for A to finish
            time.sleep(random.uniform(0.5, 1.5))  # Simulate log generation
            print("Subsystem B: Log generated")
            self.event_B_done.set()  # Signal C to start
            self.event_A_done.clear()  # Reset A event for next cycle

    def process_C(self):
        while True:
            self.event_B_done.wait()  # Wait for B to finish
            time.sleep(random.uniform(0.5, 1.5))  # Simulate log generation
            print("Subsystem C: Log generated\n")
            self.event_B_done.clear()  # Reset B event for next cycle


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
