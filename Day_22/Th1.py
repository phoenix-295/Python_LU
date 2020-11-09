import time
from threading import Thread

t1 = time.time()


def count(n):
    i = n
    while i > 0:
        i = i - 1


def count1(n):
    i = n
    while i > 0:
        i = i - 1


th1 = Thread(target=count, args=(100000000,))
th1.start()
th2 = Thread(target=count1, args=(100000000,))
th2.start()

th1.join()
th2.join()

t2 = time.time()

print("Time :", t2-t1)
