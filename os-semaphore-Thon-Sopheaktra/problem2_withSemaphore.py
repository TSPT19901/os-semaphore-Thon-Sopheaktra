import threading

a = threading.Semaphore(1)  # H starts first
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def p1():
    global a, b
    a.acquire()
    print("H", end="")
    print("E", end="")
    b.release()

def p2():
    global b, c
    b.acquire()
    print("L", end="")
    print("L", end="")
    c.release()

def p3():
    global c
    c.acquire()
    print("O", end="")

threading.Thread(target=p1).start()
threading.Thread(target=p2).start()
threading.Thread(target=p3).start()