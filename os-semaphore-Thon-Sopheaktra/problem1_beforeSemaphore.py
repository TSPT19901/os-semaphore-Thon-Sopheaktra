import threading
import time
import random

buffer = []
stop_event = threading.Event()  # shared stop signal

def producer():
    while not stop_event.is_set():       # check flag each loop
        p1 = random.randint(1, 100)
        p2 = random.randint(1, 100)
        buffer.append(p1)
        print("Produced:", p1)
        time.sleep(1)
        buffer.append(p2)
        print("Produced:", p2)
        time.sleep(1)

def consumer():
    while not stop_event.is_set():       # check flag each loop
        if len(buffer) >= 2:
            p1 = buffer.pop(0)
            p2 = buffer.pop(0)
            print("Consumed pair:", p1, p2)
        else:
            print("Consumer waiting...")
        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

try:
    while True:
        time.sleep(0.1)          # keep main thread alive, listening for Ctrl+C
except KeyboardInterrupt:
    print("\nStopping...")
    stop_event.set()             # signal both threads to stop

t1.join()
t2.join()
print("Done.")

