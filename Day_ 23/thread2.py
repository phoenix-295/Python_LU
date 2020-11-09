from threading import Thread
from queue import Queue
import random
import time

q1 = Queue()


def producer():
    while True:
        a = random.randint(1, 100)
        q1.put(a)
        time.sleep(1)
        print("Size :", q1.qsize())


def customer():
    while True:
        print(q1.get())
        time.sleep(2)


th1 = Thread(target=producer)
th1.start()

th2 = Thread(target=customer)
th2.start()

th3 = Thread(target=customer)
th3.start()
