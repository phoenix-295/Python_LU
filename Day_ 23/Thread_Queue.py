# t1 creating data
# t2 consuming data
from threading import Thread
from queue import Queue
import random
import time

q1 = Queue()  # fifo


def producer():
    while True:
        a = random.randint(1, 100)
        q1.put(a)
        time.sleep(1)
        print("Size :", q1.qsize())


def consumer():
    while True:
        print(q1.get())
        time.sleep(2)


th1 = Thread(target=producer)
th1.start()

th2 = Thread(target=consumer)
th2.start()

th3 = Thread(target=consumer)
th3.start()
