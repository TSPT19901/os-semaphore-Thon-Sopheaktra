import threading
import time

a = threading.Semaphore(1)   # starts at 1 → P1 goes first
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def p1():
    while True:
        a.acquire()          # wait for P3 to finish O
        print("H", end="")
        print("E", end="")
        b.release()          # unlock P2 twice → LL
        b.release()

def p2():
    while True:
        b.acquire()          # fires twice per cycle
        print("L", end="")
        c.release()          # each L signals P3

def p3():
    while True:
        c.acquire()          # wait for first  L
        c.acquire()          # wait for second L
        print("O", end="", flush=True)
        print()              # newline so each HELLO is on its own line
        time.sleep(0.5)      # slow it down so you can read it
        a.release()          # ← restart the chain!

threading.Thread(target=p1, daemon=True).start()
threading.Thread(target=p2, daemon=True).start()
threading.Thread(target=p3, daemon=True).start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")