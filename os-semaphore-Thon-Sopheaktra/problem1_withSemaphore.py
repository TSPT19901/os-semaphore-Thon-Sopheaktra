import threading
import time
import random

buffer = []
BUFFER_SIZE = 10
stop_event = threading.Event()

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer():
    while not stop_event.is_set():
        p1 = random.randint(1, 100)
        p2 = random.randint(1, 100)

        empty.acquire()
        empty.acquire()

        mutex.acquire()
        buffer.append(p1)
        buffer.append(p2)
        print("Produced pair:", p1, p2)
        mutex.release()

        full.release()
        full.release()

        time.sleep(0.2)

def consumer():
    while not stop_event.is_set():
        full.acquire()
        full.acquire()

        mutex.acquire()
        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print("Consumed pair:", p1, p2)
        mutex.release()

        empty.release()
        empty.release()

        time.sleep(0.3)

t1 = threading.Thread(target=producer, daemon=True)  # daemon = killed on exit
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()

try:
    while True:
        time.sleep(0.1)       # main thread stays alive
except KeyboardInterrupt:
    print("\nStopped.")
    stop_event.set()          # signal threads to stop